import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from database import SessionLocal, Message

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# ---------- DATABASE ----------
db = SessionLocal()

# ---------- SIDEBAR ----------
st.sidebar.title("💬 Chats")

if "chats" not in st.session_state:
    st.session_state.chats = ["Chat 1"]
    st.session_state.current_chat = "Chat 1"

# New chat
if st.sidebar.button("➕ New Chat"):
    new_chat = f"Chat {len(st.session_state.chats) + 1}"
    st.session_state.chats.append(new_chat)
    st.session_state.current_chat = new_chat

# Switch chats
for chat in st.session_state.chats:
    if st.sidebar.button(chat):
        st.session_state.current_chat = chat

# ---------- MAIN ----------
st.title("🤖 AI Chatbot (Groq Powered)")

# Load messages from DB
messages_db = db.query(Message).filter(
    Message.chat_name == st.session_state.current_chat
).all()

messages = [{"role": m.role, "content": m.content} for m in messages_db]

# Display chat
for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    db.add(Message(
        chat_name=st.session_state.current_chat,
        role="user",
        content=user_input
    ))
    db.commit()

    messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        placeholder = st.empty()

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )

            reply = response.choices[0].message.content
            placeholder.markdown(reply)

            # Save bot reply
            db.add(Message(
                chat_name=st.session_state.current_chat,
                role="assistant",
                content=reply
            ))
            db.commit()

        except Exception as e:
            placeholder.markdown(f"❌ Error: {e}")