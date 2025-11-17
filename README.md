# AmbedkarGPT – AI Intern Task (Kalpit Pvt Ltd)

This project is a simple **Command-Line RAG-based Question Answering System** built as part of the **AI Intern Assignment for Kalpit Pvt Ltd (UK)**.

It loads a speech by **Dr. B. R. Ambedkar**, splits it into chunks, creates embeddings, stores them locally using **ChromaDB**, and answers questions using the **Ollama LLM (Mistral / Llama3.2)** — fully offline and free.

---

## 🚀 Features

- ⚡ Fully local RAG pipeline  
- 📄 Loads and processes `speech.txt`  
- ✂️ Splits text into meaningful chunks  
- 🧠 Creates embeddings using `sentence-transformers/all-MiniLM-L6-v2`  
- 💾 Stores vectors in **ChromaDB**  
- 🔍 Retrieves relevant chunks  
- 🤖 Uses **Ollama (Mistral / Llama3.2)** for answer generation  
- 🖥️ Simple terminal-based Q&A interface  

---

## 📁 Project Structure

```
AmbedkarGPT-Intern-Task/
│── main.py
│── speech.txt
│── requirements.txt
│── README.md
│── db/ (auto-created for Chroma)
│── venv/ (optional)
```

---

## 🛠️ Installation & Setup

Follow these steps to run the project **on Windows, Mac, or Linux**.

---

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NileshVishwakarma9/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task
```

---

### 2️⃣ Create and activate virtual environment

#### **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

#### **Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Install & Setup Ollama

Download Ollama from:

👉 https://ollama.com/download

Then pull your model (Mistral 7B or Llama 3.2)

```bash
ollama pull mistral
# OR
ollama pull llama3.2
```

Ensure Ollama is running:

```bash
ollama --version
```

---

## ▶️ Running the Application

Once everything is installed, run:

```bash
python main.py
```

You should see:

```
Initializing...
System ready! Ask questions.
You:
```

Now you can start asking anything based on Ambedkar’s speech.

Example:

```
You: What is the main problem according to Ambedkar?
```

---

## 📌 Requirements (As per assignment)

- Python 3.8+
- LangChain (RAG orchestration)
- ChromaDB (vector store)
- HuggingFace Embeddings (MiniLM)
- Ollama (Mistral / Llama3.2)
- Works 100% offline
- No API keys needed

---

## 🧪 Example Queries

```
What does Ambedkar say about caste?
Why does he criticize shastras?
What is the root of the caste problem?
```

---

## 📬 Assignment Confirmation

This repository contains **all required deliverables**:

✔ `main.py` – well-commented code  
✔ `requirements.txt`  
✔ `speech.txt` (provided text)  
✔ `README.md` (setup + usage documentation)  
✔ Public GitHub repository  

---

## 🙌 Author  
**Nilesh Vishwakarma**  
AI Intern Applicant – Kalpit Pvt Ltd  

---

## 📄 License  
This project is for evaluation purposes only.
