from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

def search_liked_prompts(task_query, top_k=3):
    db = Chroma(
        persist_directory="liked_prompt_db",
        embedding_function=OllamaEmbeddings(model="mistral")
    )
    results = db.similarity_search(task_query, k=top_k)
    return "\n\n".join([doc.page_content for doc in results])