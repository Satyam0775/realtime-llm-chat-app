# realtime-llm-chat-app
# 🧠 Real-Time LLM Chat App

This project is a real-time, multi-user chat application using a local LLM via Ollama, built with:

- 🔄 FastAPI + Socket.IO (backend)
- 🧾 Streamlit (frontend)
- 🐋 Docker Compose (for containerization)
- 🧠 Ollama (for running LLMs like Mistral locally)

---

## 🚀 Features

- Real-time chat over Socket.IO
- Async communication between backend & frontend
- Multi-user support
- LLM-powered replies using `mistral` model via Ollama
- Containerized deployment with Docker

---

## 🛠️ Setup Instructions

### 📦 Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Ollama](https://ollama.com/) installed locally
- Model `mistral` installed locally:
  ```bash
 ollama run mistral

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

