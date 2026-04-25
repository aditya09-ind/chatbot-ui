🤖 AI Chatbot (Groq Powered)

A ChatGPT-like AI chatbot built using Streamlit, Groq API, and SQLite with a clean UI, multi-chat support, and persistent chat history.

---

🚀 Live Demo

👉 https://chatbot-uigit-j7e3mat6wykr9r5pxg8rck.streamlit.app/

---

✨ Features

- 💬 ChatGPT-like UI using Streamlit
- ⚡ Fast responses powered by Groq (Llama 3 models)
- 📂 Multiple chat sessions (sidebar support)
- 🧠 Chat history stored using SQLite
- 🔐 Secure API key handling using Streamlit Secrets
- 🌐 Deployed on Streamlit Cloud

---

🛠️ Tech Stack

- Frontend: Streamlit
- Backend: Python
- AI Model: Groq (Llama 3.1)
- Database: SQLite (SQLAlchemy ORM)
- Deployment: Streamlit Community Cloud

---

📁 Project Structure

chatbot-ui/
│
├── app.py              # Main Streamlit app
├── database.py         # Database (SQLite + SQLAlchemy)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

---

⚙️ Installation (Run Locally)

1. Clone the repository:

git clone https://github.com/aditya09-ind/chatbot-ui.git
cd chatbot-ui

2. Create virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Create ".env" file:

GROQ_API_KEY=your_api_key_here

5. Run the app:

streamlit run app.py

---

🔑 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Select repo and deploy "app.py"
4. Add secret:

GROQ_API_KEY = "your_api_key_here"

---

⚠️ Notes

- SQLite database resets on Streamlit Cloud (temporary storage)
- For production, use a cloud database like Supabase or Firebase

---

📸 Screenshots

<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/74b2fec2-2f3f-44c7-bd05-dd6c7bf51778" />


---

🧠 Future Improvements

- 🔐 User authentication (login system)
- ☁️ Cloud database integration
- 🎤 Voice input support
- 📄 File upload + AI chat
- 💾 Persistent chat memory

---

👨‍💻 Author

Aditya Tripathi

- GitHub: https://github.com/aditya09-ind

---

⭐ Contributing

Feel free to fork this repo and improve it!

---

📜 License

This project is open-source and available under the MIT License.
