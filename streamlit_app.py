import streamlit as st
import socketio
import threading

# Initialize Socket.IO client
sio = socketio.Client()

# Streamlit session states
if "messages" not in st.session_state:
    st.session_state.messages = []
if "connected" not in st.session_state:
    st.session_state.connected = False
if "connection_error" not in st.session_state:
    st.session_state.connection_error = ""

# Handle backend responses
@sio.on("response")
def handle_response(data):
    st.session_state.messages.append((data["user"], data["message"]))
    st.experimental_rerun()

# Thread function to connect
def connect_to_backend():
    try:
        sio.connect("http://backend:8000")  # Use Docker Compose service name
        st.session_state.connected = True
    except Exception as e:
        st.session_state.connection_error = str(e)
        st.session_state.connected = False

# Streamlit UI
st.set_page_config(page_title="🧠 Chat with Local LLM", layout="centered")
st.title("🧠 Chat with Local LLM")

username = st.text_input("Enter your name", "User")

# Connect Button
if not st.session_state.connected:
    if st.button("🔌 Connect to Backend"):
        threading.Thread(target=connect_to_backend).start()
        st.info("Trying to connect...")

if st.session_state.connection_error:
    st.error(f"Connection failed: {st.session_state.connection_error}")

# Message Input and Send
prompt = st.text_input("Your message:")
if st.button("📤 Send"):
    if not st.session_state.connected:
        st.warning("⚠️ Connect to the backend first.")
    elif prompt.strip():
        st.session_state.messages.append((username, prompt))
        sio.emit("message", {"prompt": prompt, "user": username})

# Display Chat History
st.markdown("---")
for user, msg in st.session_state.messages:
    st.markdown(f"**{user}**: {msg}")
