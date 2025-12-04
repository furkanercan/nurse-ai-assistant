import streamlit as st
import requests
import os

st.set_page_config(page_title="NurseGame RAG Chat", layout="wide")
st.title("🩺 NurseGame Patient Chat")

# Welcome section with key information
with st.expander("ℹ️ About This Demo", expanded=True):
    st.markdown("""
    ### 👋 Welcome!
    
    This is a **legacy version** of an AI nurse assistant, originally developed for a separate project.
    
    **📋 Important Information:**
    - 🎯 **Demo Purpose**: This deployment is for demonstration and testing purposes only
    - 🏥 **Synthetic Data**: All patient data is **not real** and is generated for demonstration
    - 🔒 **Privacy Protected**: There is **no PII (Personally Identifiable Information)** in this system
    - ⚠️ **Not for Medical Use**: This tool should not be used for actual medical diagnosis or treatment
    
    Select a patient from the sidebar and start asking questions to explore the AI assistant's capabilities!
    """)

# Get backend URL from environment variable, with fallback for local development
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip('/')

patient_id = st.sidebar.selectbox("Select Patient", [f"patient{i}" for i in range(1, 9)])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask a question about the patient...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(
            f"{BACKEND_URL}/ask",
            json={"question": user_input, "patient_id": patient_id},
            timeout=10
        )
        answer = response.json().get("answer", "⚠️ No answer found.")
    except Exception as e:
        answer = f"⚠️ Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
