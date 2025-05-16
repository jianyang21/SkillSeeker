# Skill Seeker 🎯

**Skill Seeker** is an AI-powered Streamlit application that helps job seekers refine their resumes. It uses a T5 language model to intelligently extract and summarize key skills and information from resumes, stores the results securely in Firebase, and sends the corrected content via email.

## 🚀 Features

- 📄 Upload resumes in PDF format
- 🤖 Extract and summarize resume content using a T5 LLM
- 🔍 Identify key skills and areas of improvement
- 🧠 Grammar correction and content enhancement
- 🔐 Store data securely using Firebase
- 📧 Send results to the user via email
- ⚡ Minimal, responsive UI built with Streamlit

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**:
  - [T5 Language Model](https://huggingface.co/transformers/model_doc/t5.html) (via HuggingFace Transformers)
  - [Firebase](https://firebase.google.com/) (for real-time database/storage)
  - [smtplib](https://docs.python.org/3/library/smtplib.html) for email integration
- **Libraries**:
  - `transformers`, `firebase-admin`, `python-docx`, `PyMuPDF`, etc.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jingyang21/skill-seeker.git
   
   cd skill-seeker
