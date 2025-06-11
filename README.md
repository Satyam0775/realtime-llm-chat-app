# realtime-llm-chat-app
# 🧠 Real-time Chat with Local LLM (Generative AI Internship Assignment)

This is a real-time, multi-user chat system using a local LLM (via Ollama), built with FastAPI, Socket.IO, and Streamlit. Fully containerized using Docker Compose.

## 🚀 Features

- 🔄 Real-time communication via Socket.IO
- 🧑‍🤝‍🧑 Supports multiple users
- 🧠 Powered by Mistral / LLaMA 3 running on Ollama
- 🧊 Easy deployment using Docker Compose
- 🖥️ Clean UI using Streamlit

---

## 🧱 Architecture

- **Backend**: FastAPI + Socket.IO
- **Frontend**: Streamlit + Socket.IO client
- **LLM**: Local model running on Ollama (e.g., Mistral)
- **Communication**: Asynchronous, event-based

---

## ⚙️ Setup Instructions

### 1. Install [Ollama](https://ollama.com) and pull a model:
```bash
ollama pull mistral
ollama serve
git clone https://github.com/yourusername/genai-realtime-chat.git
cd genai-realtime-chat
#docker-compose up --build

Frontend: http://localhost:8501
Backend API: http://localhost:8000

🧪 Example Use
Click "Connect to Server"

Enter your name

Type your question

Get LLM-powered response in real-time

