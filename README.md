# LLM PDF Summary Chatbot
Upload any PDF and start chatting with it — all processed locally with your own LLM.
🔒 100% private: works offline using Ollama and open-source tools.

### 🚀 Demo
Upload a PDF → Ask a question → Get smart answers based on its content.


### 🔧 Features
- 📥 Upload any .pdf (contracts, research, etc.)

- 🤖 Local LLM (LLaMA 3 via Ollama)

- 🧠 Context-aware Q&A

- 💬 Gradio-based chat interface

- 🔐 Fully offline (no external APIs)

### 📦 Installation
```
git clone https://github.com/ryu878/LLM-PDF-Summary-Chatbot.git
cd LLM-PDF-Summary-Chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ▶️ Run the App

1. Start Ollama:
```
ollama run llama3

```

2. Start the chatbot:
```
python app.py

```

### 📁 Project Structure
```
📦 LLM-PDF-Summary-Chatbot/
├── app.py               # Gradio UI
├── llm_chat.py          # LLM query logic (Ollama)
├── pdf_parser.py        # PDF text extractor
├── requirements.txt     # Python deps
└── README.md
```

### 📜 License
MIT — free to use, modify, and share.

### ✅ TODOs
- Add summarization button (one-click)

- Multiple PDF support

- Chunked vector search (FAISS)

- Save Q&A session to file

- Vector-based semantic search (e.g., ChromaDB/FAISS)



## Contacts
To contact me please pm:

Telegram: https://t.me/ryu8777

Discord: https://discord.gg/zSw58e9Uvf
