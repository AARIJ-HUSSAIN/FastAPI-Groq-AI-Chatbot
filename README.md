# AI Chatbot (FastAPI + Groq + ChatGPT Style UI)

An end-to-end AI chatbot application built using **FastAPI (backend)** and **Groq LLM API**, with a modern **ChatGPT-style frontend UI** and **persistent chat memory**.

---

## Features

### AI Capabilities

* Powered by Groq LLM (`llama-3.1-8b-instant`)
* Context-aware responses (chat memory)
* System prompt for controlled behavior

### Chat Interface

* Full-screen ChatGPT-style UI
* Dark mode design
* Chat bubbles (user + AI)
* Typing indicator
* Auto-scroll

### Smart Rendering

* Markdown support (bold, lists, headings)
* Clean and readable AI responses

### Memory System

* Backend memory (context-aware conversation)
* Frontend memory (localStorage → persists after refresh)

---

## Tech Stack

* **Backend:** FastAPI
* **LLM API:** Groq
* **Frontend:** HTML, CSS, JavaScript
* **Markdown Rendering:** Marked.js
* **Environment Management:** python-dotenv

---

## Project Structure

```
AI-Chatbot/
│── main.py
│── index.html
│── requirements.txt
│── .env.example
│── .gitignore
│── LICENSE
│── README.md
```

---

## Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add your API key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub

---

### 5️⃣ Run backend

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 6️⃣ Run frontend

Just open:

```
index.html
```

in your browser.

---

## How It Works

```
User → Frontend UI → FastAPI → Groq LLM → Response → UI Rendering
```

* Frontend sends user message
* Backend sends message + history to LLM
* LLM generates response
* Frontend renders response using Markdown

---

## Security Notes

* `.env` is ignored using `.gitignore`
* API keys are never exposed in the repository
* Use `.env.example` for reference

---

## Future Improvements

* User authentication system
* Database memory (SQLite / MongoDB)
* Streaming responses (real-time typing)
* Deploy to cloud (Render / Vercel)
* Mobile responsive UI

---

## License

This project is licensed under the MIT License.

---

## Author

Aarij Hussain

---

## Contribution

Feel free to fork, improve, and submit pull requests.

---

## Final Note

This project demonstrates a **full-stack AI application** combining:

* Backend API development
* LLM integration
* Frontend UI design
* Memory handling

