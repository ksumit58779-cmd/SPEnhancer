# SPEnhancer
An app that turns your basic prompt to magic prompt which give incredible output 
# ✦ AI Prompt Enhancer

> Transform simple prompts into powerful, high-quality prompts using AI.

---

## 🚀 Features

- **3 Enhancement Levels** — Normal, Pro, Extremely Pro
- **Shimmer Sweep Animation** — Apple Intelligence-style reveal effect
- **Magic Sound Effects** — Immersive audio on every enhancement
- **Prompt History** — Auto-saves every enhanced prompt
- **Prompt Library** — 30+ ready-to-use prompts across 6 categories
- **Search & Filter** — Find any prompt instantly
- **Copy & Reuse** — One click to copy or send to enhancer

---

## 📁 Project Structure

```
AI-PROMPT-ENHANCER/
│
├── Backend/
│   ├── app.py                  # Flask server (entry point)
│   ├── enhancer.py             # Gemini AI enhancement logic
│   ├── history_mananger.py     # Save/load prompt history
│   └── prompt_library.py      # Prompt library manager
│
├── frontend/
│   ├── index.html              # Main enhancer page
│   ├── history.html            # Prompt history page
│   └── library.html           # Prompt library page
│
├── css/
│   ├── main.css                # Global styles & variables
│   ├── animations.css          # All animation effects
│   └── components.css         # UI components
│
├── js/
│   ├── main.js                 # App logic & API calls
│   ├── animation.js            # Shimmer sweep engine
│   ├── sound.js                # Sound effects manager
│   └── library.js             # Library search & filter
│
├── assets/
│   ├── sounds/
│   │   └── magic.mp3           # Magic reveal sound
│   └── icons/
│       └── logo.svg            # App logo
│
├── data/
│   ├── history.json            # Prompt history (auto-created)
│   └── prompts_library.json   # Prompt library (auto-created)
│
├── .env                        # API keys (never commit this!)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## ⚙️ Setup & Installation

### 1. Clone or download the project

```bash
cd AI-PROMPT-ENHANCER
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key to `.env`

```
GEMINI_API_KEY=your_actual_key_here
```

Get a free key at: https://aistudio.google.com/app/apikey

### 4. Run the server

```bash
cd Backend
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

```
User types prompt
      ↓
Sends to Flask (app.py) via POST /api/enhance
      ↓
enhancer.py calls Gemini AI with mode-specific system prompt
      ↓
Enhanced prompt returned to frontend
      ↓
Shimmer sweep animation plays ✨
Magic sound effect plays 🎵
History auto-saved 💾
```

---

## 🎯 Enhancement Modes

| Mode | What It Does |
|------|-------------|
| ⚡ Normal | Cleans up wording, adds clarity |
| 🚀 Pro | Structured, detailed, optimized |
| 💎 Extremely Pro | Professional-grade with full context, constraints, and output format |

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| AI | Google Gemini (gemini-1.5-flash) |
| Frontend | HTML + CSS + JavaScript |
| Animations | CSS + Web Animations API |
| Sound | Web Audio API + MP3 |
| Storage | JSON files |

---

## 📦 API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/api/enhance` | Enhance a prompt |
| GET | `/api/history` | Get all history |
| DELETE | `/api/history/clear` | Clear all history |
| GET | `/api/library` | Get prompts (optional `?category=`) |
| GET | `/api/library/search` | Search prompts (`?q=keyword`) |

---

## 🔐 Environment Variables

```
GEMINI_API_KEY=your_key_here
```

> ⚠️ Never commit your `.env` file to GitHub!

---

## 📱 Mobile (Coming Soon)

The app will be packaged as an Android APK using Android Studio.

---

Built with 🔥 by a developer who means business.
