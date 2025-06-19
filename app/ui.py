import streamlit as st
from gtts import gTTS
import uuid
import os

def render_sidebar():
    st.sidebar.subheader("MongoDB Dataset")
    st.sidebar.markdown("This agent uses a fixed MongoDB dataset.")
    return st.sidebar.button("Process")

def render_chat():
    user_input = st.chat_input("Ask something...")

    if "voice_text" in st.session_state and st.session_state.voice_text:
        user_input = st.session_state.voice_text
        st.session_state.voice_text = ""

    if user_input:
        with st.spinner("Thinking..."):
            from app.agent import process_query
            response = process_query(user_input)
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("agent", response))

    if "audio_cache" not in st.session_state:
        st.session_state.audio_cache = {}

    for idx, (role, msg) in enumerate(st.session_state.chat_history):
        with st.chat_message(role):
            st.markdown(msg)
            if role == "agent":
                col1, col2 = st.columns([0.9, 0.1])
                with col2:
                    if st.button("🔈", key=f"tts_{idx}"):
                        if idx not in st.session_state.audio_cache:
                            tts = gTTS(text=msg)
                            filename = f"tts_{uuid.uuid4().hex}.mp3"
                            tts.save(filename)
                            st.session_state.audio_cache[idx] = filename
                        st.audio(st.session_state.audio_cache[idx], format="audio/mp3")

    if st.sidebar.button("New Conversation"):
        st.session_state.chat_history = []
        if "audio_cache" in st.session_state:
            for path in st.session_state.audio_cache.values():
                if os.path.exists(path):
                    os.remove(path)
            st.session_state.audio_cache = {}

