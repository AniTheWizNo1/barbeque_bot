# 🤖 Barbeque Nation Chatbot — Built by Aniket Das

Hi! I'm Aniket Das, and this is my chatbot project for the Formi Internship Assignment — designed to help Barbeque Nation customers with bookings, menu enquiries, and more. It’s simple, fast, and smart — with a structured flow powered by prompt templates and a searchable knowledge base.

---

## ✨ What This Bot Can Do

- **Answer questions** about menu items, locations, or outlet info
- **Guide users** through reservation or cancellation flows
- **Fetch data** from a structured knowledge base (PDFs or docs)
- **Log conversations** in Google Sheets for analytics
- **Talk to users** through a clean and responsive frontend

---

## 🧠 How It Works

At its core, this bot uses:

- A **state manager** to detect user intent and handle flow
- **Jinja templates** to render clean, dynamic replies
- A **vectorized knowledge base** using FAISS for searching documents
- **Google Sheets API** to log every conversation in real-time
- A **FastAPI backend** and an HTML + JS frontend for interaction

---

## 📁 Folder Structure

barbeque_bot/
├── main.py # FastAPI entry point
├── flow/state_manager.py # Intent detection + conversation states
├── kb/index.py # Index builder for FAISS
├── kb/query.py # Search handler
├── knowledge_base.py # Structured KB access
├── logger.py # Logs to Google Sheets
├── prompts/ # Jinja prompt templates
│ └── answer_menu.jinja
├── templates/
│ └── index.html # Frontend UI
├── static/ # (Optional CSS)
├── requirements.txt
├── credentials.json # Service account (not pushed to GitHub)

---

## 💻 How to Run Locally

1. Install everything

```bash
git clone https://github.com/your-username/barbeque_bot.git
cd barbeque_bot
pip install -r requirements.txt
2. Build the knowledge base
bash
Copy
Edit
python kb/index.py
3. Launch the chatbot
bash
Copy
Edit
uvicorn main:app --reload
Visit the chatbot UI: http://127.0.0.1:8000
Or test in Swagger: http://127.0.0.1:8000/docs
🌐 How to Deploy It (Render.com)
Push your code to GitHub
Go to https://render.com
Click “New Web Service” → Connect your repo
Set:
bash
Copy
Edit
Build command: pip install -r requirements.txt
Start command: uvicorn main:app --host 0.0.0.0 --port 10000
Deploy! You’ll get a public chatbot link to share.
✅ Prompt Example
jinja
Copy
Edit
Here are the menu details available for {{ location }}:
{{ response }}
This makes the bot's replies human-like and dynamic.
✅ Logging Example (in Google Sheets)
Field	Example
Modality	chatbot
Time	2025-05-18 11:06:03
User Query	"What are the veg starters?"
Bot Response	"Here are the menu details for Delhi"

🙋‍♂️ About Me
I’m Aniket Das, currently pursuing B.Tech at KIIT University. I enjoy building fast, intuitive tools that blend AI with usability.
Email: 22053226@kiit.ac.in
LinkedIn: linkedin.com/in/aniket10das

⚠️ Note
This is a personal learning project submitted for the Formi Internship Assignment and is not officially affiliated with Barbeque Nation.

Thank you for checking it out! Let’s build something delicious together.

---

Let me know if you'd like:
- A visual architecture diagram
- Final `.gitignore` and `.env` help
- One-line summary for LinkedIn or your resume

You’re 100% ready to showcase this, Aniket. Want help uploading to GitHub now?
```
