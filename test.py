import requests
import os

# Configure backend URL - change this to test different backends
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
# For deployed testing, use: BACKEND_URL = "https://nurse-ai-assistant.onrender.com"

# Test questions - uncomment the one you want to test
test_question = "Tell me the name, age, gender, race, ethnicity, weight, height, religion, mother, favorite animal and sexual activity history of the patient."
# test_question = "Tell me about the sensory perception of this patient."
# test_question = "Tell me about the surgical history of this patient."
# test_question = "Tell me about the religion of this patient."

print(f"Testing backend at: {BACKEND_URL}")
print(f"Question: {test_question}")
print(f"Patient: patient1")
print("-" * 60)

try:
    response = requests.post(
        f"{BACKEND_URL.rstrip('/')}/ask",
        json={
            "patient_id": "patient1",
            "question": test_question
        },
        timeout=30
    )
    
    if response.status_code == 200:
        result = response.json()
        print("SUCCESS!")
        print(f"\nAnswer:\n{result.get('answer', 'No answer found')}")
    else:
        print(f"ERROR: Status code {response.status_code}")
        print(f"Response: {response.text}")
        
except requests.exceptions.ConnectionError:
    print(f"Connection Error: Could not connect to {BACKEND_URL}")
    print("   Make sure the backend is running and the URL is correct.")
except requests.exceptions.Timeout:
    print(f"Timeout: Backend took too long to respond")
except Exception as e:
    print(f"Error: {e}")
