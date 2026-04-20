from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os

# STEP 1: load .env file
load_dotenv()

# STEP 2: get API key from .env
api_key = os.getenv("GROQ_API_KEY")

# STEP 3: create Groq client
client = Groq(api_key=api_key)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Chatbot running"}

@app.get("/chat")
def chat(message: str):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": message}
        ]
    )

    return {
        "user": message,
        "ai": response.choices[0].message.content
    }