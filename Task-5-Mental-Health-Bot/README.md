# Task 5: Mental Health Support Chatbot (Fine-Tuned)

## 📌 Overview
This project involves fine-tuning a **DistilGPT2** model on the **EmpatheticDialogues** dataset to create a supportive mental health chatbot. The model was trained to recognize emotional context and respond with empathy.

## 🧠 Training Details
* **Model:** DistilGPT2 (Small, efficient Causal LM).
* **Dataset:** EmpatheticDialogues (CSV format).
* **Preprocessing:** Combined User inputs and Agent responses into a single conversation stream: `User: ... \nBot: ...`.
* **Training Size:** 5,000 examples trained for 3 epochs on a T4 GPU.

## ⚙️ Inference Strategy
To prevent "babbling" or repetition, the inference pipeline uses:
* `temperature=0.6` (Focused responses)
* `repetition_penalty=1.3` (Prevents looping phrases)
* `max_new_tokens=50` (Concise answers)

## 🚀 How to View
Open `Task5_Mental_Health_FineTuning.ipynb` to view the full training pipeline, loss logs, and conversation examples.