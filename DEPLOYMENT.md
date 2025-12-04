# Deployment Guide

This guide will help you deploy this project to Streamlit Cloud and set up the backend.

## Architecture Overview

- **Frontend**: Streamlit app (`rag_chat_ui.py`) deployed to Streamlit Cloud
- **Backend**: FastAPI app (`app.py`) deployed to Render/Railway/etc.

## Step 1: Deploy the Backend

### Option A: Deploy to Render (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `nurse-chat-backend` (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     - `OPENAI_API_KEY`: Your OpenAI API key
5. Click "Create Web Service"
6. Wait for deployment to complete
7. **Copy the service URL** (e.g., `https://nurse-chat-backend.onrender.com`)

### Option B: Deploy to Railway

1. Go to [Railway](https://railway.app/)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variable:
   - `OPENAI_API_KEY`: Your OpenAI API key
5. Railway will auto-detect Python and deploy
6. **Copy the service URL** from the deployment

## Step 2: Deploy to Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click "New app"
4. Configure:
   - **Repository**: Select this repository
   - **Branch**: `main` (or your default branch)
   - **Main file path**: `rag_chat_ui.py`
   - **App URL**: You can customize this or use the default
5. Click "Advanced settings"
6. Add **Secrets** (Environment Variables):
   ```
   BACKEND_URL=https://your-backend-url.onrender.com
   ```
   Replace `https://your-backend-url.onrender.com` with your actual backend URL from Step 1.
7. Click "Deploy"
8. Wait for deployment to complete

## Step 3: Disconnect from Old Project

### If the old project is on Streamlit Cloud:

1. Go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Find the old app connected to `https://nurse-chat.streamlit.app/`
3. You have two options:

   **Option A: Update the existing app (Recommended)**
   - Click on the old app
   - Go to "Settings"
   - Change the repository to point to this new repository
   - Update the main file path if needed
   - Update the environment variables (especially `BACKEND_URL`)
   - Click "Save"
   - The app will redeploy with the new code

   **Option B: Delete and recreate**
   - Click on the old app
   - Go to "Settings" → "Delete app"
   - Confirm deletion
   - Follow Step 2 above to create a new app
   - Use the same app URL: `nurse-chat`

### If the old project is on a different platform:

1. Simply update the Streamlit Cloud app to point to this repository (as described in Option A above)
2. The old deployment will continue running but won't be updated

## Step 4: Verify Deployment

1. Visit your Streamlit app: `https://nurse-chat.streamlit.app/`
2. Select a patient from the sidebar
3. Ask a test question
4. Verify that:
   - The question appears in the chat
   - The backend responds correctly
   - No errors appear

## Troubleshooting

### Backend not responding
- Check that the backend URL in Streamlit secrets is correct
- Verify the backend is running (visit the backend URL directly)
- Check backend logs for errors

### Environment variables not working
- In Streamlit Cloud, go to "Settings" → "Secrets"
- Ensure `BACKEND_URL` is set correctly
- Redeploy the app after changing secrets

### Local testing
- Set `BACKEND_URL` environment variable locally:
  ```bash
  export BACKEND_URL=http://localhost:8000  # Linux/Mac
  set BACKEND_URL=http://localhost:8000     # Windows CMD
  $env:BACKEND_URL="http://localhost:8000"  # Windows PowerShell
  ```
- Or run the backend locally and the app will default to `http://localhost:8000`

## Environment Variables Reference

### Backend (Render/Railway)
- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Frontend (Streamlit Cloud)
- `BACKEND_URL`: URL of your deployed backend (required)

