# Instructions to Disconnect from Old Project

This guide will help you disconnect the old project from `https://nurse-chat.streamlit.app/` and connect it to this new project.

## Option 1: Update Existing Streamlit App (Recommended)

This is the easiest approach - you'll update the existing Streamlit Cloud app to point to this new repository.

### Steps:

1. **Go to Streamlit Cloud Dashboard**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Find Your App**
   - Look for the app that's currently deployed at `https://nurse-chat.streamlit.app/`
   - Click on it to open the app settings

3. **Update Repository**
   - Click on "Settings" (or the gear icon)
   - In the "Repository" section, click "Edit"
   - Change the repository to point to this new repository:
     - Repository: `your-username/nurse-chat-knowledgeable` (or whatever this repo is called)
     - Branch: `main` (or your default branch)
     - Main file path: `rag_chat_ui.py`

4. **Update Environment Variables**
   - Scroll down to "Secrets" section
   - Add or update the `BACKEND_URL` secret:
     ```
     BACKEND_URL=https://your-new-backend-url.onrender.com
     ```
   - Replace with your actual new backend URL (from Render/Railway/etc.)
   - If you haven't deployed the backend yet, see [DEPLOYMENT.md](DEPLOYMENT.md) Step 1

5. **Save and Deploy**
   - Click "Save" at the bottom
   - Streamlit will automatically redeploy the app
   - Wait for deployment to complete (usually 1-2 minutes)

6. **Verify**
   - Visit `https://nurse-chat.streamlit.app/`
   - Test the app to ensure it's working with the new backend
   - The old project will no longer be connected

## Option 2: Delete and Recreate

If you prefer a clean slate:

1. **Delete Old App**
   - Go to Streamlit Cloud Dashboard
   - Find the app at `nurse-chat.streamlit.app`
   - Click on it → "Settings" → "Delete app"
   - Confirm deletion

2. **Create New App**
   - Follow the deployment steps in [DEPLOYMENT.md](DEPLOYMENT.md) Step 2
   - When creating the app, use the app name: `nurse-chat`
   - This will give you the same URL: `https://nurse-chat.streamlit.app/`

## Option 3: Keep Both (Different URLs)

If you want to keep the old project running:

1. **Create New App with Different Name**
   - Follow [DEPLOYMENT.md](DEPLOYMENT.md) Step 2
   - Use a different app name (e.g., `nurse-chat-v2`)
   - This will give you a new URL: `https://nurse-chat-v2.streamlit.app/`

2. **Old Project Continues**
   - The old project at `nurse-chat.streamlit.app` will continue working
   - You can delete it later when you're ready

## What Happens to the Old Project?

- **If you update the existing app (Option 1)**: The old code will be replaced, and the app will use this new repository
- **If you delete and recreate (Option 2)**: The old app is completely removed
- **If you keep both (Option 3)**: Both apps run independently

## Troubleshooting

### "App not found" error
- Make sure you're signed into the correct GitHub account
- Check that the repository name is correct

### App not updating
- Wait a few minutes for Streamlit to redeploy
- Check the deployment logs in Streamlit Cloud
- Verify the repository and branch are correct

### Backend connection errors
- Verify `BACKEND_URL` is set correctly in Streamlit secrets
- Make sure your backend is deployed and running
- Test the backend URL directly in your browser

## Need Help?

If you encounter issues:
1. Check the deployment logs in Streamlit Cloud
2. Verify all environment variables are set correctly
3. Ensure the backend is running and accessible
4. See [DEPLOYMENT.md](DEPLOYMENT.md) for more details

