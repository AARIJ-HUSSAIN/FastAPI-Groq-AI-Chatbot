from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 MEMORY STORE (simple in RAM)
chat_history = []

@app.get("/chat")
def chat(message: str):

    # add user message
    chat_history.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            *chat_history
        ]
    )

    answer = response.choices[0].message.content

    # add assistant message
    chat_history.append({"role": "assistant", "content": answer})

    return {
        "response": answer
    }