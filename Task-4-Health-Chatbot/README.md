# Task 4: AI Health Assistant (Streamlit App)

## 📌 Overview
An interactive web-based chatbot powered by **Google Gemini 1.5 Flash**. It provides general health and wellness advice while adhering to strict safety guardrails (refusing medical diagnoses).

## 🛠️ Features
* **Prompt Engineering:** System instructions ensure the bot acts as a helpful assistant, not a doctor.
* **Streamlit GUI:** A clean, chat-style interface for easy interaction.
* **Security:** Uses `.env` for secure API key management.

## ⚙️ Configuration
To run this locally, create a file named `.env` in this folder and add your Google Gemini API key:
```text
GOOGLE_API_KEY=your_actual_api_key_here