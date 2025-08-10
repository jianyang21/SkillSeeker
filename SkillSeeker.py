import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.schema import Document
import os

st.set_page_config(page_title="PDF Q&A with RAG")
st.title("PDF Q&A with LangChain RAG")

# Session state to store QA chain
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "pdf_ready" not in st.session_state:
    st.session_state.pdf_ready = False

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and not st.session_state.pdf_ready:
    # Save uploaded file temporarily
    temp_path = "temp_uploaded.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load PDF
    loader = PyPDFLoader(temp_path)
    data = loader.load()

    # Split into chunks
    text = "\n".join([d.page_content for d in data])
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Create embeddings & vector store
    embeddings = OllamaEmbeddings(model="llama3")
    vectorstore = FAISS.from_documents(docs, embeddings)

    # LLaMA model
    llm = Ollama(model="llama3")

    # Retrieval QA
    st.session_state.qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    st.session_state.pdf_ready = True
    st.success("PDF processed. You can now ask questions.")

# If PDF is processed, allow multiple questions
if st.session_state.pdf_ready and st.session_state.qa_chain:
    query = st.text_input("Ask a question about the PDF")

    if query:
        with st.spinner("Thinking..."):
            result = st.session_state.qa_chain.invoke({"query": query})

        # Show result
        st.subheader("Answer")
        st.write(result["result"])

        # Show sources
        with st.expander("Source Chunks"):
            for i, doc in enumerate(result["source_documents"]):
                st.markdown(f"**Chunk {i+1}:**\n{doc.page_content}")

