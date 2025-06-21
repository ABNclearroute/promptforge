# PromptForge — Local AI Prompt Assistant

PromptForge is a local CLI tool that:
- Suggests prompts using Ollama-hosted LLMs
- Lets you provide feedback
- Remembers only the prompts you liked
- Uses them in future prompt suggestions with Retrieval-Augmented Generation (RAG)
- Supports tagging for future retrieval

## Requirements

- Python 3.8+
- Ollama installed: https://ollama.com
- A local model pulled, e.g.:

```bash
ollama pull mistral
