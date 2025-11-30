import os
from dotenv import load_dotenv
from groq import Groq
import time

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Error: GROQ_API_KEY is missing from .env")

client = Groq(api_key=api_key)

# Chat memory
chat_history = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant like ChatGPT. "
                   "You respond clearly, naturally, and politely."
                    
                    "You speak in a friendly and natural way. "
                    "You reply clearly and politely."
    }
]

def stream_reply(prompt):
    chat_history.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=chat_history,
        stream=True
    )

    print("Bot:", end=" ", flush=True)
    final_text = ""

    for chunk in response:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            text = delta.content
            final_text += text

            for ch in text:
                print(ch, end="", flush=True)
                time.sleep(0.008)

    print()
    chat_history.append({"role": "assistant", "content": final_text})


if __name__ == "__main__":
    print("\nChatGPT-Style Groq Chatbot")
    print("----------------------------")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "by"]:
            print("Bot: Goodbye! 😊")
            break

        stream_reply(user_input)
