# AI Chatbot using Groq API

## Description

This is a backend AI chatbot built using FastAPI and Groq API.
It generates intelligent responses using LLM (LLaMA models).

## Features

* FastAPI backend
* Chat endpoint using Groq API
* Fast responses using LLaMA models
* Secure API key handling with environment variables

## Tech Stack

* Python
* FastAPI
* Groq API

##  How to Run

1. Clone repo
2. Create `.env` file and add your API key:

   ```
   GROQ_API_KEY=your_key_here
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Run server:

   ```
   uvicorn main:app --reload
   ```

## Endpoint

```
/chat?message=your_message
```

## Note

Frontend UI will be added in future updates.
