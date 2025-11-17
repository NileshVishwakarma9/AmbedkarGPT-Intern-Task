# AmbedkarGPT-Intern-Task

## Overview
AmbedkarGPT is a command-line Q&A system that answers questions based on a short excerpt from Dr. B.R. Ambedkar's "Annihilation of Caste".

It uses **LangChain**, **ChromaDB**, **HuggingFace embeddings**, and **Ollama (Mistral 7B)**.

---

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository_url>
cd AmbedkarGPT-Intern-Task
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Ollama & pull Mistral 7B:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull mistral
```

---

## Usage
Run the system:
```bash
python main.py
```

Type your questions and AmbedkarGPT will answer based on the speech.  
Type `exit`, `quit`, or `bye` to close the program.

---

## Files
- `main.py` → Core Python code.
- `speech.txt` → Text excerpt for the Q&A.
- `requirements.txt` → Python dependencies.
- `README.md` → Instructions and overview.
