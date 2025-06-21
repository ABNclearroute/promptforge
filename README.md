# 🛠️ PromptForge

**PromptForge** is your personal, evolving prompt engineering assistant — built to help you think better, not just prompt better.

This is not just a prompt generator. It's a *learning assistant* that:
- Suggests high-quality prompts tailored to your tasks
- Stores and tags successful prompts for reuse
- Uses Retrieval-Augmented Generation (RAG) with vector search
- Offers A/B testing for iterative improvement
- Collects feedback and auto-scores prompt quality
- Runs locally with open models (Ollama) and supports custom OpenAI-compatible endpoints

> 📚 Designed by someone who believes in lifelong learning and builds small POCs every weekend to sharpen real-world skills.

---

## 🔍 Why PromptForge?

When working with LLMs, prompt quality determines outcome quality. But in fast-paced environments, we often:

- Don’t spend enough time crafting prompts
- Forget what worked in the past
- Struggle to iterate and improve
- Get stuck rewriting from scratch

**PromptForge** solves this by turning prompting into a structured, feedback-driven process.

---

## ✨ Features

- ✅ Local prompt generation using Ollama (`mistral`, `llama3`, etc.)
- 🔁 Feedback loop: Was the prompt helpful? Rate and comment
- 📥 Auto-ingests liked prompts into RAG context for future queries
- 🧠 Vector search on liked prompts using `langchain + chromadb`
- 🧪 A/B Testing mode for comparing prompt variations
- 🧾 Prompt scoring powered by Gemini (via custom API)
- 🏷️ Tagging support to filter prompts by task domain (e.g., `resume`, `performance testing`)
- 🧹 Full reset support to clear prompt memory and start fresh

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/your-username/promptforge.git
cd promptforge
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you also have:

- [Ollama installed](https://ollama.com/download)
- A local model pulled (e.g., `ollama pull mistral`)

### 3. Run the assistant

```bash
python main.py
```
---

## How It Works

```txt
[You] ──> Describe your task
            ↓
[PromptForge] ──> Suggest prompt(s) using local LLM + past prompt context
            ↓
[You] ──> Try the prompt elsewhere (ChatGPT, Claude, etc.)
            ↓
[PromptForge] ──> Ask for feedback + auto-score the prompt
            ↓
Liked prompts stored and reused contextually
```

---

## Tech Stack

| Component | Role |
|----------|------|
| **Python** | CLI & logic |
| **Ollama** | Local LLM inference |
| **LangChain** | RAG pipeline & chaining |
| **ChromaDB** | Vector storage for liked prompts |
| **SQLite** | Prompt feedback + metadata |
| **Gemini API** | Prompt scoring (via OpenAI-compatible client) |

---

## Feedback Loop

Every time you use PromptForge:
- It gets better at generating helpful prompts
- Your best prompts are saved and reused
- You build your personal prompt memory over time


---

## Ideal For

- Software engineers using LLMs in their daily tasks
- Test automation and QA engineers
- Resume/job seekers customizing LLM outputs
- Prompt engineers exploring A/B styles
- Anyone committed to **learning in public** and iterative improvement

---