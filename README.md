<img width="54" height="54" alt="Neon Orbital N Emblem" src="https://github.com/user-attachments/assets/642843ca-cc0a-4157-acb1-884126e9db89" />

# BOT NYRA - Your AI Companion

**BOT NYRA** is a lightweight AI assistant web app built with Flask. It helps with everyday questions, creative ideas and productivity, and comes with a built-in email summarizer.

---

## ✨ Features

- **💬 Ask NYRA Anything** - Chat with an AI companion to get thoughtful answers, explanations and creative ideas.
- **✉️ Email Summarizer** - Paste a long email and get a short, clear summary.
- **🌙 Clean dark UI** - Simple, responsive interface that works on desktop and mobile.

---

## 🛠️ Tech Stack

| Layer      | Technology                                  |
|------------|---------------------------------------------|
| Backend    | Python, Flask |
| AI         | OpenAI and Google GenAI SDK |
| Config     | python-dotenv |
| Frontend   | HTML templates + static CSS/JS/assets       |

---

## 📁 Project Structure

```
bot-nyra/
├── main.py            # Flask app: routes and AI logic
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates
├── static/            # CSS, JS, images (e.g. logo.png)
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or newer
- An API key for the AI provider(s) the app uses (OpenAI and/or Google Gemini)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Butkii025/bot-nyra.git
cd bot-nyra

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root and add your API key(s). The variable names below are examples; use the names that `main.py` reads.

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_google_gemini_api_key
```

### Run Locally

```bash
python main.py
```

Then open **http://127.0.0.1:5000** in your browser.

## visual

<img width="1207" height="835" alt="image" src="https://github.com/user-attachments/assets/73e56283-14c7-4be2-b054-b8d16002694b" />

---

## 📦 Dependencies

```
flask
openai
python-dotenv
google-genai
```

---

## 🔒 Security Notes

- Keep API keys in environment variables, never in source code.
- Consider adding rate limiting to public AI endpoints to avoid abuse and unexpected costs.
- Avoid pasting sensitive or confidential emails into any third-party AI service.

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome. Feel free to open an issue or submit a pull request.

---

## 👤 Author

Developed by **Priyanshu** - [Portfolio](https://p-vijay.vercel.app)

---
