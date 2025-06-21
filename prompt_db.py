import sqlite3
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

conn = sqlite3.connect("prompt_history.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ab_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    prompt_a TEXT,
    prompt_b TEXT,
    chosen TEXT,
    tag TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def save_ab_test_result(task, prompt_a, prompt_b, chosen, tag):
    cursor.execute(
        "INSERT INTO ab_tests (task, prompt_a, prompt_b, chosen, tag) VALUES (?, ?, ?, ?, ?)",
        (task, prompt_a, prompt_b, chosen, tag)
    )
    conn.commit()

def save_prompt(task, prompt, feedback, tag):
    cursor.execute(
        "INSERT INTO prompts (task, prompt, feedback, tag) VALUES (?, ?, ?, ?)",
        (task, prompt, feedback, tag)
    )
    conn.commit()

def save_liked_prompt_to_rag(task, prompt, tag):
    embedding_model = OllamaEmbeddings(model="mistral")
    doc = Document(page_content=prompt, metadata={"task": task, "tag": tag})
    db = Chroma(
        persist_directory="liked_prompt_db",
        embedding_function=embedding_model
    )
    db.add_documents([doc])

def view_prompts_by_tag(tag):
    cursor.execute("SELECT prompt FROM prompts WHERE tag = ?", (tag,))
    return [row[0] for row in cursor.fetchall()]