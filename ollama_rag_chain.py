from langchain_ollama import OllamaLLM  # Previously Ollama
from langchain_core.prompts import PromptTemplate
from liked_rag import search_liked_prompts

llm = OllamaLLM(model="mistral")

template = """
You are a prompt generator assistant.

Your job is to take a user goal and suggest a prompt they can paste into ChatGPT or another LLM to accomplish that goal.

IMPORTANT:
- Do NOT write the story, answer the question, or perform the task.
- DO NOT explain anything.
- ONLY generate a single prompt in plain English that the user can paste into ChatGPT or Claude.

User Goal:
{task}

Relevant past prompts:
{context}

OUTPUT:
<Your prompt here>
"""

prompt_template = PromptTemplate.from_template(template)
chain = prompt_template | llm

def generate_prompt_with_liked_prompt_rag(task):
    context = search_liked_prompts(task)
    return chain.invoke({"task": task, "context": context})


def generate_ab_prompts(task):
    context = search_liked_prompts(task)

    # Template A: Formal
    template_a = PromptTemplate.from_template("""
You are a prompt generator assistant. Provide a high-quality, professional prompt that a user can paste into ChatGPT or Claude to achieve their goal.
Task:
{task}
Relevant past prompts:
{context}
""")
    
    # Template B: Concise
    template_b = PromptTemplate.from_template("""
You're a prompt assistant. Create a short, focused prompt based on this task:
{task}
Here are some related prompts:
{context}
""")

    prompt_a = (template_a | llm).invoke({"task": task, "context": context})
    prompt_b = (template_b | llm).invoke({"task": task, "context": context})
    return prompt_a.strip(), prompt_b.strip()