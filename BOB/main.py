import os
import json
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

# Set Groq API Key
os.environ["GROQ_API_KEY"] = "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"

HISTORY_FILE = "bob_history.json"

# ✅ Ensure history file exists (create if missing)
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

# Load history from file
def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
            return [
                HumanMessage(content=m["content"]) if m["role"] == "human" else AIMessage(content=m["content"])
                for m in data
            ]
    except Exception as e:
        print("⚠️ Couldn't read history:", e)
        return []

# Save history to file
def save_history(history):
    try:
        data = []
        for msg in history:
            role = "human" if isinstance(msg, HumanMessage) else "ai"
            data.append({"role": role, "content": msg.content})
        with open(HISTORY_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("⚠️ Couldn't save history:", e)

# Initialize model
llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.7)

# Load chat history
history = load_history()

# First run: Tell BOB who he is
if not history:
    intro_msg = "You are BOB (Bot of bots), a smart and witty chatbot. Your name is always BOB. Never forget it. Introduce yourself to the user, also add that your name's full form is Bot of Bots. Don't add bragging or self-praise. Just be kind, and act like any human being. After 1 or 2 sentences, go to next line."
    history.append(HumanMessage(content=intro_msg))
    reply = llm.invoke(history)
    history.append(AIMessage(content=reply.content))
    save_history(history)
    print("BOB:", reply.content)

# Begin chat
print("\n🤖 Chat with BOB (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower().strip() in ["exit", "quit"]:
        save_history(history)
        print("BOB: Bye! 👋")
        break

    history.append(HumanMessage(content=user_input))
    response = llm.invoke(history)
    print("BOB:", response.content)
    history.append(AIMessage(content=response.content))
    save_history(history)