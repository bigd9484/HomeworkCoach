# HomeworkCoach

An open-source Python agent that acts as a virtual school assistant.  
It reads mock assignment data, breaks tasks into steps via an LLM, and quizzes your child with a local math model—all driven by simple voice (console) prompts.

---

## 🚀 Features

- **Fetch assignments** from a JSON “portal” (`school_portal.json`)
- **LLM-powered breakdown**: Uses OpenAI (or Claude) to turn each assignment into step-by-step instructions
- **Math quiz**: Generates mock math problems and checks answers
- **Voice-style interaction** via `input()` prompts (can be extended to real TTS/ASR)

---

## 🏗️ Architecture

┌─────────────────┐
│ school_portal.json │
└────────┬────────┘
│ load
▼
┌───────────────────────────┐
│ HomeworkCoach (main.py) │
│ ┌───────────────────────┐ │
│ │ 1. load_assignments() │ │
│ │ 2. breakdown_steps() │ │
│ │ 3. quiz_student() │ │
│ └───────────────────────┘ │
└─────────────┬─────────────┘
│ calls
▼
┌──────────────┐
│ OpenAI API │ ← or Claude endpoint
└──────────────┘
│
▼
┌──────────────┐
│ Console I/O │
└──────────────┘

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone** the repo:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/HomeworkCoach.git
   cd HomeworkCoach
Create & activate a virtualenv (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API key (for OpenAI):

bash
Copy
Edit
export OPENAI_API_KEY="your_api_key_here"
▶️ Usage
bash
Copy
Edit
python main.py
You’ll be prompted to select an assignment and then guided through step-by-step breakdowns and quizzes.

📄 Mock Data
Include a school_portal.json in the repo root, for example:


🤝 Contributing
Fork the repo

Create a new branch (git checkout -b feature/awesome)

Commit your changes

Open a Pull Request

Made with ❤️ for smarter homework sessions!
