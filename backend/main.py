from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your frontend to call this endpoint
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Keep your webhook URL here (hidden from the frontend)
WEBHOOK_URL = "https://ai-symbo.app.n8n.cloud/webhook/zaya"

@app.get("/get-webhook")
def get_webhook():
    return {"webhook": WEBHOOK_URL}
