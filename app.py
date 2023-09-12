import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
from llama_index import SimpleDirectoryReader

st.set_page_config(page_title="Chat with the Streamlit", page_icon="G", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Chat with the Streamlit")
