# SkillSeeker

This is a Streamlit web application that allows you to upload a PDF file, process it using LangChain, FAISS, and Ollama, and then ask questions about its content. It uses Retrieval-Augmented Generation (RAG) to provide accurate answers based on the document.

## Features
- Upload a PDF file
- Process the document once and reuse it for multiple questions
- Uses FAISS for vector storage and retrieval
- Displays relevant source text for each answer
- Ask unlimited questions until you close the app

## LLM Model
This application uses the LLaMA 3 model through Ollama for both embeddings and answering questions.

## Requirements
- Python 3.10 or later
- Streamlit
- LangChain with langchain_community modules
- FAISS
- Ollama installed locally and running
- LLaMA 3 model pulled in Ollama

## Installation

1. Install dependencies  
   `pip install streamlit langchain faiss-cpu pypdf langchain-community`

2. Install and set up Ollama  
   Download from https://ollama.ai/download  
   Pull the LLaMA 3 model:  
   `ollama pull llama3`

## Running the App
Run:  
`streamlit run app.py`  

Open your browser at http://localhost:8501.

## How It Works
1. Upload a PDF file
2. The file is read, split into chunks, and embedded using Ollama embeddings
3. The embeddings are stored in a FAISS vector store
4. When you ask a question, the most relevant chunks are retrieved and passed to the LLaMA 3 model
5. The model returns an answer along with the relevant source text

## Notes
- Ollama must be running in the background
- To change the model, update the `Ollama(model="...")` call in the code
