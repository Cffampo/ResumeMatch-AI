# 📄 ResumeMatch AI

https://resumematch-ai-carlfampo.streamlit.app/

> An intelligent resume analyzer powered by Google Gemini that delivers ATS-style feedback, skill gap analysis, and actionable career coaching — in seconds.

<img width="3199" height="799" alt="Screenshot 2026-05-06 140506" src="https://github.com/user-attachments/assets/dd910d1a-67e4-4c97-a9b7-ce18dd1665d4" />


![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Flash-4285F4?style=flat&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 🚀 What It Does

ResumeMatch AI helps job seekers instantly understand how their resume stacks up against any job description. Upload a PDF resume, optionally paste a job posting, and get:

- **Candidate Summary** — a concise breakdown of experience and qualifications
- **Key Skills Extraction** — automatically identified competencies
- **Actionable Improvements** — targeted suggestions to make the resume more recruiter-ready
- **ATS-Style Scoring** — a weighted score across four categories, visualized as an interactive bar chart
- **Downloadable Report** — export the full analysis as a `.txt` file

---

## 🧠 Technical Highlights

| Area | Detail |
|---|---|
| **LLM Integration** | Google Gemini Flash (`gemini-flash-lite-latest`) via the `google-generativeai` SDK |
| **PDF Parsing** | `PyPDF2` with intelligent text normalization (preserves paragraph structure while collapsing inline newlines) |
| **Structured Output** | Prompt engineered to return a hybrid response — human-readable analysis + machine-parseable JSON in a single generation |
| **Data Visualization** | Scores parsed from JSON and rendered as a `st.bar_chart` + `st.progress` meter |
| **UI** | Multi-column Streamlit layout with expander, spinner, and download button for a clean, responsive experience |

---

## 🏗️ Architecture

```
User uploads PDF
      │
      ▼
PyPDF2 extracts & cleans text
      │
      ▼
Streamlit UI collects optional job description
      │
      ▼
Structured prompt sent to Gemini Flash
      │
      ├── Analysis text  ──► Rendered in UI
      └── Score JSON     ──► Parsed → bar chart + progress bar
```

---

## 💡 Skills Demonstrated

- **Prompt Engineering** — Designed a single prompt that produces structured JSON embedded in natural language output, then parses both halves reliably
- **LLM API Integration** — Configured and called the Gemini API with proper error handling and environment-based key management
- **PDF Text Extraction** — Handled multi-page PDFs with regex-based text normalization for clean downstream processing
- **Data Parsing & Visualization** — Safely parsed LLM-generated JSON and mapped it to interactive Streamlit charts with graceful fallback on parse failure
- **Full-Stack Python App** — End-to-end application from file upload to AI analysis to downloadable report, using only Python

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/resumematch-ai.git
cd resumematch-ai

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install streamlit google-generativeai PyPDF2 python-dotenv pandas

# Set up your environment variables
cp .env.example .env
# Add your GEMINI_API_KEY to .env

# Run the app
streamlit run main.py
```

---

## 🗂️ Project Structure

```
AI Resume Analyzer/
├── .env.example        # Environment variable template
├── .gitignore
├── .streamlit/
│   └── config.toml     # Streamlit theme/config
├── main.py             # Main application
├── README.md
└── venv/               # Virtual environment (not committed)
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google AI Studio API key |

Get a free key at [aistudio.google.com](https://aistudio.google.com).

---

## 📸 How It Works

1. **Upload** your resume as a PDF
2. **Paste** a job description (optional, but recommended for tailored feedback)
3. **Click** "Analyze Resume"
4. **Review** the AI-generated analysis, score breakdown, and chart
5. **Download** the full report

---

## 🔮 Future Improvements

- [ ] Support for `.docx` resume uploads
- [ ] Side-by-side diff view of resume vs. job description keywords
- [ ] Multiple job description comparison
- [ ] Persistent history with a database backend
- [ ] Cover letter generation based on gap analysis


## 📄 License

MIT — free to use, modify, and distribute.
