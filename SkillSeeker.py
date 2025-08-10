import streamlit as st
from pypdf import PdfReader
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Firebase credentials file path
FIREBASE_CRED_PATH = "firebase_credentials.json"  # Change if needed

# ---- Streamlit UI ----
st.set_page_config(page_title="SkillSeeker")
st.title("SkillSeeker")
st.header("Analyzing Candidate Resume and Skills")

# Name input
st.subheader("Write your name")
name = st.text_input("Enter your name here")

# Role input
st.subheader("Enter the role you are applying for")
role = st.text_input("Enter your desired role")

# Upload Resume
st.subheader("Upload your resume")
uploaded_resume_file = st.file_uploader("Resume (PDF only)", type="pdf")

# Initialize Firebase only once
if not firebase_admin._apps:
    if os.path.exists(FIREBASE_CRED_PATH):
        cred = credentials.Certificate(FIREBASE_CRED_PATH)
        firebase_admin.initialize_app(cred)
    else:
        st.error(f"Firebase credentials file not found at: {FIREBASE_CRED_PATH}")

# Firestore client
resume_db = firestore.client()

# Process Resume
if uploaded_resume_file is not None:
    st.success("Resume uploaded successfully!")
    reader = PdfReader(uploaded_resume_file)
    resume_text = "".join([page.extract_text() + "\n" for page in reader.pages])
    
    # Store data in Firestore
    if name and role:
        doc_ref = resume_db.collection("ExtractedContent").document(name)
        doc_ref.set({
            "name": name,
            "role_applied": role,
            "resume_text": resume_text
        })
        st.success("Resume data saved to Firebase!")
    else:
        st.warning("Please enter both name and role to save data.")

    # Display extracted text
    st.subheader("Extracted Resume Text")
    st.write(resume_text)
else:
    st.info("Please upload a resume.")

# Upload JD
st.subheader("Upload the Job Description (JD)")
uploaded_JD_Resume = st.file_uploader("Job Description (PDF only)", type="pdf", key="jd")

if uploaded_JD_Resume is not None:
    st.success("JD uploaded successfully!")
else:
    st.info("Please upload a JD.")


