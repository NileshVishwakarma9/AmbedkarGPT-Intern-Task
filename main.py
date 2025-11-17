from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
import os


# --------------------------------------------
# BUILD VECTOR DATABASE (only once)
# --------------------------------------------
def build_vectorstore():
    print("Building vector DB...")

    loader = TextLoader("speech.txt", encoding="utf-8")d
    documents = loader.load()

    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=300,
        chunk_overlap=50,
        length_function=len,
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="db"
    )

    vectordb.persist()
    return vectordb


# --------------------------------------------
# LOAD VECTOR DB + LLM
# --------------------------------------------
def load_system():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    llm = Ollama(model="llama3.2")   # FAST and GOOD

    return vectordb, llm


# --------------------------------------------
# ANSWER FUNCTION
# --------------------------------------------
def answer_question(query, vectordb, llm):

    # 1 → retrieve best matching document chunks
    docs = vectordb.similarity_search(query, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are AmbedkarGPT.

Answer the question using the context below.
If answer not found in context, still respond naturally.

Context:
{context}

Question: {query}

Answer:
"""

    # 2 → call Ollama
    response = llm.invoke(prompt)

    return response


# --------------------------------------------
# MAIN LOOP
# --------------------------------------------
if __name__ == "__main__":
    print("Initializing...")

    # build DB once
    if not os.path.exists("db"):
        build_vectorstore()

    vectordb, llm = load_system()

    print("System ready! Ask questions.\n")

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        answer = answer_question(query, vectordb, llm)
        print("AmbedkarGPT:", answer, "\n")
