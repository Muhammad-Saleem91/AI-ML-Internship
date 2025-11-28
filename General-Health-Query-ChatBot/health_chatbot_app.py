import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="HealthBot AI", page_icon="🏥")

# --- 1. LOAD API KEY SECURELY ---
load_dotenv() # This loads the variables from .env
api_key = os.getenv("GOOGLE_API_KEY")

# --- 2. CHECK IF KEY EXISTS ---
if not api_key:
    st.error("❌ API Key not found!")
    st.stop() # Stop the app if no key is found

# --- 3. CONFIGURE GEMINI ---
genai.configure(api_key=api_key)

# --- 4. APP UI ---
st.title("🏥 AI Health Assistant")
st.markdown("Ask me general health questions! (e.g., *'How to improve sleep?'* or *'Benefits of drinking water?'*)")
st.info("Powered by Google Gemini | Task 4 Prompt Engineering")

# --- 5. DEFINE SYSTEM PROMPT ---
system_instruction = """
You are a helpful, empathetic, and clear AI medical assistant.
Your goal is to provide general health information, hygiene tips, and wellness advice.

CRITICAL SAFETY RULES:
1. You are NOT a doctor. Do NOT provide diagnoses, interpret lab results, or prescribe medication.
2. Communicate with them in a clear politely manner.
3. If a user asks about a life-threatening emergency (e.g., chest pain, trouble breathing, severe bleeding), IMMEDIATELY tell them to call emergency services.
"""

# --- 6. CHAT SESSION MANAGEMENT ---
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=system_instruction)
    st.session_state.chat_session = model.start_chat(history=[])

# --- 7. DISPLAY CHAT HISTORY ---
for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# --- 8. HANDLE USER INPUT ---
if user_input := st.chat_input("Type your health question here..."):
    # Show User Message
    st.chat_message("user").markdown(user_input)
    
    try:
        # Get AI Response
        response = st.session_state.chat_session.send_message(user_input)
        
        # Show AI Message
        with st.chat_message("assistant"):
            st.markdown(response.text)
            
    except Exception as e:
        st.error(f"Error: {e}")