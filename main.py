import streamlit as st
from app.ui import render_sidebar, render_chat
from app.agent import initialize_agent, process_query
from app.db import connect_to_mongo, load_collections
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Conversational DB Agent", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "agent" not in st.session_state:
    st.session_state.agent = None
if "db" not in st.session_state:
    st.session_state.db = None

st.sidebar.title("Dataset Control")
process_clicked = render_sidebar()

if process_clicked:
    st.session_state.db = connect_to_mongo()

    if st.session_state.db is not None:
        st.success("Database connected.")
    else:
        st.error("Failed to connect to MongoDB.")

    st.session_state.agent = initialize_agent(st.session_state.db)

    if st.session_state.agent:
        st.success("Agent initialized.")
    else:
        st.error("Failed to initialize agent.")

    st.success("Database processed and agent initialized.")

st.title("Conversational Agent for MongoDB")
if st.session_state.agent:
    render_chat()
else:
    st.info("Please click 'Process' in the sidebar to begin.")
