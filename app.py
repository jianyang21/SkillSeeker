from flask import Flask, render_template, request, jsonify
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.schema import Document
import os
import tempfile

app = Flask(__name__)

# Store vectorstore globally so it persists between requests
vectorstore = None
qa_chain = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():
    global vectorstore, qa_chain

    if "pdf" not in request.files:
        return jsonify({"error": "No PDF file uploaded"}), 400

    pdf_file = request.files["pdf"]

    # Save uploaded PDF to a temporary file
    temp_path = os.path.join(tempfile.gettempdir(), pdf_file.filename)
    pdf_file.save(temp_path)

    # Load and split PDF
    loader = PyPDFLoader(temp_path)
    data = loader.load()
    text = "\n".join([d.page_content for d in data])
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Create embeddings & vectorstore
    embeddings = OllamaEmbeddings(model="llama3")
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Initialize QA chain
    llm = Ollama(model="llama3")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    return jsonify({"message": "PDF uploaded and processed successfully."})

@app.route("/ask", methods=["POST"])
def ask_question():
    global qa_chain
    if not qa_chain:
        return jsonify({"error": "No PDF processed yet."}), 400

    data = request.json
    query = data.get("question", "")

    if not query:
        return jsonify({"error": "Question is empty."}), 400

    result = qa_chain.invoke({"query": query})
    return jsonify({
        "answer": result["result"],
        "sources": [doc.page_content for doc in result["source_documents"]]
    })

if __name__ == "__main__":
    app.run(debug=True)
