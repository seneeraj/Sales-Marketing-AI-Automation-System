
# 📄 `README.md`

```markdown
# 🚀 Sales & Marketing AI Automation System

An Sales & Marketing AI Automation System to **generate content, capture leads, convert clients, and analyze performance** — all in one dashboard.

Built using **Streamlit + Ollama (LLM) + SQLite**, this project demonstrates a real-world AI product architecture.

---

## 🌟 Features

### ✍️ AI Content Generation
- Generate multiple LinkedIn posts using local LLM (Ollama)
- Supports tone selection:
  - Viral
  - Expert
  - Storytelling

### 🎯 Lead Generation
- Upload CSV or generate leads dynamically
- Intelligent lead scoring

### 📧 Conversion Engine
- Generate personalized email responses for high-quality leads

### 📊 Analytics Dashboard
- Lead score distribution chart
- Conversion funnel visualization
- Key performance metrics

### 💾 Persistent Storage
- Save posts to SQLite database
- View saved posts
- Delete posts anytime

### 🔗 LinkedIn Integration (Manual)
- One-click “Post to LinkedIn” (prefilled content)

---

## 🧠 System Architecture

```

User Input
↓
Orchestrator (Decision Engine)
↓
Agents
├── Content Agent (Ollama)
├── Lead Agent
├── Conversion Agent
└── Analytics Agent
↓
Streamlit Dashboard + SQLite

````

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Ollama (Gemma / Mistral / LLaMA) |
| Database | SQLite |
| Visualization | Matplotlib |
| Data Handling | Pandas |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone (The Repository)
cd ai-growth-system
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install & Run Ollama

Download:
👉 [https://ollama.com](https://ollama.com)

Run model:

```bash
ollama run gemma3:4b
```

OR:

```bash
ollama run mistral
```

---

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```

ai_growth_system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── agents/
│   ├── orchestrator.py
│   ├── content_agent.py
│   ├── lead_agent.py
│   ├── conversion_agent.py
│   ├── analytics_agent.py
│
├── utils/
│   └── db.py
│
├── data/
│   └── posts.db (auto-created)

```

---

## 📊 Example Use Case

Input:

```

Generate leads, create LinkedIn content, convert clients, and show analytics for my AI marketing agency

```

Output:

* ✅ 3–5 AI-generated LinkedIn posts
* ✅ Lead table with scoring
* ✅ Personalized email responses
* ✅ Analytics graphs (distribution + funnel)
* ✅ Save & manage posts

---

## 🚀 Key Highlights

* 🔥 Multi-agent AI system
* 🧠 Local LLM (no API cost)
* ⚡ Real-time dashboard
* 💾 Persistent storage
* 📊 Business-ready analytics

---

## ⚠️ Limitations

* LinkedIn posting is manual (API requires OAuth approval)
* Performance depends on local machine (LLM inference)
* Single-user system (multi-user coming soon)

---

## 🔮 Future Improvements

* 🔐 Multi-user login system
* 📅 Post scheduling
* 🤖 Auto-post to LinkedIn (via API)
* 📈 Advanced analytics (trend tracking)
* ⭐ Favorite / tag posts
* 🌐 Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Neeraj Bhatia**

* AI & Data Science Enthusiast
* Building real-world AI products

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share with others
👉 Build on top of it 🚀

---
