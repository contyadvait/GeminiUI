import os
import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = os.getenv("gemini_api_key")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def generative_response(prompt):
    try:
        reponse = chat.send_message(prompt)
        return reponse.text
    except:
        return "Sorry, something went wrong. Please do not send content that can be flagged by the system.\nFor example,\n1. Sexually Explicit Content\n2. Hate speech\n3. Harrassment\n4. Dangerous Content of any sort"

prompt = st.text_input("What do you want to ask Gemini?")
with st.button():
    st.text("Submit")