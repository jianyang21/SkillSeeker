# SkillSeeker

This repository contains two separate applications that allow you to upload a PDF file, process it using LangChain, FAISS, and Ollama, and then ask questions about its content. Both use Retrieval-Augmented Generation (RAG) to provide accurate answers based on the document.

## Applications Included
1. **Streamlit Web App**
2. **Flask App with HTML/CSS Frontend**

---

## 1. Streamlit Version

### Features
- Upload a PDF file
- Process the document once and reuse it for multiple questions
- Uses FAISS for vector storage and retrieval
- Displays relevant source text for each answer
- Ask unlimited questions until you close the app

### LLM Model
Uses the LLaMA 3 model through Ollama for embeddings and answering questions.

### Requirements
- Python 3.10 or later
- Streamlit
- LangChain with `langchain_community` modules
- FAISS
- Ollama installed locally and running
- LLaMA 3 model pulled in Ollama

### Installation
1. Install dependencies  
   ```bash
   pip install streamlit langchain faiss-cpu pypdf langchain-community

## 2. Flask + HTML/CSS Version


## Flask App Folder Structure

pdf_rag_app/
│
├── app.py 
│
├── templates/ 
│ └── index.html 
│
├── static/ 
   └── style.css


### Features
- Simple HTML/CSS user interface
- Upload a PDF
- Ask unlimited questions without re-uploading
- Displays answer and relevant document context

### LLM Model
Uses the LLaMA 3 model through Ollama for embeddings and answering questions.

### Requirements
- Python 3.10 or later
- Flask
- LangChain with `langchain_community` modules
- FAISS
- pypdf
- Ollama installed locally and running
- LLaMA 3 model pulled in Ollama

### Installation
1. Install dependencies  
   ```bash
   pip install flask langchain langchain-community faiss-cpu pypdf
