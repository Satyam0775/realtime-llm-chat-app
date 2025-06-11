from fastapi import FastAPI
import socketio
import requests

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
app = FastAPI()
app.mount("/", socketio.ASGIApp(sio))

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

@sio.event
async def connect(sid, environ):
    print(f"✅ User connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"❌ User disconnected: {sid}")

@sio.event
async def message(sid, data):
    prompt = data.get("prompt", "")
    user = data.get("user", "User")

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        response_json = response.json()
        reply = response_json.get("response", "⚠️ Error: No response from LLM")
    except Exception as e:
        reply = f"❌ LLM Error: {e}"

    await sio.emit("response", {"user": "LLM", "message": reply}, to=sid)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("llm_chat_backend:app", host="0.0.0.0", port=8000)

