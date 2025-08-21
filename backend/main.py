# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Allow frontend access (restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hidden n8n webhook URL (keep secret)
N8N_WEBHOOK_URL = "https://ai-symbo.app.n8n.cloud/webhook/zayaHealthInsuranceAssistant"

@app.post("/chat")
async def chat(request: Request):
    """
    Receive JSON: { session_id, message, files: [{ filename, content }, ...] }
    Proxy the JSON to N8N_WEBHOOK_URL and return the response.
    """
    try:
        payload = await request.json()
    except Exception as e:
        return {"error": "Invalid JSON: " + str(e)}

    try:
        # Forward payload to n8n webhook
        resp = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=60)
        resp.raise_for_status()
        # Return whatever n8n returns (assumed JSON)
        return resp.json()
    except Exception as e:
        return {"error": "Failed to call webhook: " + str(e)}
