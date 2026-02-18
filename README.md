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



***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, liquidations, volume, delta, liquidity, spread behavior, funding)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL, ClickHouse
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***
