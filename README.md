# Nurse Chat - RAG Knowledgeable

A medical chat application with RAG (Retrieval Augmented Generation) capabilities for patient data queries.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- OpenAI API key

### Local Development

1. **Set up virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\Activate.ps1
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables:**
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="sk-your-key-here"
   $env:BACKEND_URL="http://localhost:8000"  # Optional, defaults to localhost:8000
   
   # Linux/Mac
   export OPENAI_API_KEY="sk-your-key-here"
   export BACKEND_URL="http://localhost:8000"  # Optional
   ```

4. **Run the backend:**
   ```bash
   uvicorn app:app --reload
   ```
   Backend will be available at `http://localhost:8000`

5. **Run the Streamlit frontend (in a new terminal):**
   ```bash
   streamlit run rag_chat_ui.py
   ```
   Frontend will open at `http://localhost:8501`

## 🐳 Docker

```bash
docker build -t nurse-chat-backend .
docker run -p 8000:8000 -e OPENAI_API_KEY=sk-... nurse-chat-backend
```

## 📦 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to:
- Streamlit Cloud (frontend)
- Render/Railway (backend)

## 🔗 Disconnecting from Old Project

If you're migrating from an old project connected to `https://nurse-chat.streamlit.app/`:

1. Go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Find the app connected to `nurse-chat.streamlit.app`
3. Update the repository to point to this new repository
4. Update environment variables (set `BACKEND_URL` to your new backend)
5. Save and redeploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

## 📁 Project Structure

```
├── app.py                 # FastAPI backend
├── rag_chat_ui.py        # Streamlit frontend
├── data/                  # Patient data with embeddings
│   └── patient1-8/
│       ├── chunks.json
│       └── *_embedded_chunks.json
├── embed_all_patients.py  # Script to generate embeddings
└── requirements.txt       # Python dependencies
```

## 🔑 Environment Variables

### Backend
- `OPENAI_API_KEY` (required): Your OpenAI API key

### Frontend
- `BACKEND_URL` (optional): Backend API URL, defaults to `http://localhost:8000`