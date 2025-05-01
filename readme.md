# 📚 Research Assistant

This project implements an **agentic AI research assistant** that searches arXiv for academic papers, downloads and summarizes them, and generates markdown-based flashcards — all in an automated, containerized flow using **Docker Compose**.

The goal is to combine **local LLM inference (via Ollama)** with lightweight tools for PDF processing and summarization, allowing you to go from query → paper → summary → flashcards seamlessly.

---

## 🧠 Agentic Flow

```
User → CLI / Frontend
        ↓
     🥉 Agent (FastAPI)
        ↓ issues tool calls
    ┌─────────────────────────────────────┐
    │ 1. arxiv-search-api        │ → gets paper links
    │ 2. pdf-downloader          │ → downloads & extracts text
    │ 3. summarizer              │ → condenses paper to key ideas
    │ 4. flashcard-generator     │ → creates Q&A markdown
    └─────────────────────────────────────┘
        ↓
     Agent aggregates output
        ↓
     Flashcards.md returned or saved
```

---

## 🛠️ Services

| Component              | Description                            |
|------------------------|----------------------------------------|
| **Agent**              | FastAPI server that orchestrates tools |
| **LLM (Ollama)**       | Runs `gemma3:1b` locally                |
| **Search Tool**        | arXiv API client                       |
| **PDF Downloader**     | Downloads and extracts paper content   |
| **Summarizer**         | Summarizes extracted text              |
| **Flashcard Generator**| Creates markdown flashcards            |

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/research-agent
cd research-agent
```

### 2. Start the System
Ensure Docker is installed and running, then execute:
```bash
docker compose up --build
```

> This will start:
> - The Agent API (`localhost:8000`)
> - Ollama with `gemma3:1b` (`localhost:11434`)

---

### 3. Test the Flow

Once all services are up, test the pipeline using:

#### With `curl`:
```bash
curl -X POST 'http://localhost:8000/agent' \
  -H 'Content-Type: application/json' \
  -d '{"query": "Graph Neural Networks"}'
```

#### With Python (optional):
```python
import requests
res = requests.post("http://localhost:8000/agent", json={"query": "Graph Neural Networks"})
print(res.json())
```

---

## ✅ Output

You will receive a structured JSON containing:
- Paper metadata
- Summarized insights
- A markdown-formatted set of Q/A flashcards

---

## 🧰 Tool Breakdown

### 🧠 Agent (FastAPI)
Coordinates tool calls in sequence: search → download → summarize → flashcards.

### 🔎 Arxiv Search
Fetches top papers related to the user query using the arXiv API.

### 📄 PDF Downloader
Downloads PDFs from arXiv links and extracts clean text using PyMuPDF.

### 📝 Summarizer
Uses `gemma3:1b` (via Ollama) to generate key insights from the paper.

### 🃏 Flashcard Generator
Transforms the summary into active recall Q&A flashcards in Markdown format.

---

## 📌 Notes

- Ollama downloads the `gemma3:1b` model on first run (can take a few minutes).
- All components run in **isolated Docker containers**.
- Next steps: Add UI, support external PDFs, add persistent storage.

