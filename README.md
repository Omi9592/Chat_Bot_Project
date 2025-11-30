🧠 Auto Replay AI Chatbot (Groq Version)

A fast, ChatGPT-style AI chatbot powered by Groq’s free Llama-3.3 model.
This project includes:

ChatGPT-style streaming responses

Conversation memory

Secure API key handling using .env

Clean project structure

100% free to run (Groq API)

🚀 Features

Streaming AI replies (type-as-you-see effect)

Llama-3.3-70B — extremely fast & capable

Safe API key setup (no key in code)

Continuous conversation memory

Cross-platform (Windows / Mac / Linux)

📁 Project Structure
Auto_Replay_AI_Chatbot_Project/
│── app/
│   │── chatbot.py
│   │── __init__.py
│
│── .env
│── .gitignore
│── requirements.txt
│── README.md

🔐 Setup API Key (Very Important)
1. Get your free Groq API Key

Create a free key from:

👉 https://console.groq.com/keys

You’ll get something like:

gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

2. Put the key inside .env
GROQ_API_KEY=your_real_key_here


⚠ DO NOT upload .env to GitHub.
Your .gitignore already protects it.

📦 Install Required Libraries

Run:

pip install -r requirements.txt


Contents of requirements:

groq
python-dotenv

▶️ Run the Chatbot

Inside the project root:

python app/chatbot.py


You’ll see:

ChatGPT-Style Groq Chatbot
----------------------------
You:


Now type freely.

To exit:

exit
quit
bye

🧩 How It Works
✔ Loads API key securely
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

✔ Uses Groq’s Llama 3.3 Model
model="llama-3.3-70b-versatile"

✔ Streams the response word-by-word
for chunk in response:
    text = chunk.choices[0].delta.content

✔ Maintains chat history
chat_history.append({"role": "user", "content": prompt})

🛡 Security Notes

API key is never stored in the code

.env file is ignored by git

Safe for public GitHub repositories
