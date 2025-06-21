from prompt_db import save_prompt, save_liked_prompt_to_rag, view_prompts_by_tag, save_ab_test_result
from ollama_rag_chain import generate_prompt_with_liked_prompt_rag, generate_ab_prompts
from feedback import collect_feedback, score_prompt

def start_prompt_assistant():
    print("Welcome to PromptForge — your evolving prompt assistant.")
    print("Type 'exit' to quit, or 'view <tag>' to see prompts by tag.\n")

    while True:
        task = input("What do you want to accomplish? ").strip()
        if task.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if task.lower().startswith("view "):
            tag = task[5:].strip()
            prompts = view_prompts_by_tag(tag)
            print(f"\n--- Prompts for tag: {tag} ---")
            for i, p in enumerate(prompts, 1):
                print(f"\n[{i}] {p}\n")
            print("------------------------------\n")
            continue

        tag = input("Give a tag to this task (e.g., performance, resume): ").strip()

        ab_mode = input("Do you want to A/B test prompts for this task? (y/n): ").strip().lower()
        if ab_mode == "y":
            prompt_a, prompt_b = generate_ab_prompts(task)
            print("\nPrompt A:\n", prompt_a)
            print("\nPrompt B:\n", prompt_b)
            choice = input("\nWhich prompt do you prefer? (1/2): ").strip()

            chosen = "A" if choice == "1" else "B"
            selected_prompt = prompt_a if chosen == "A" else prompt_b
            save_ab_test_result(task, prompt_a, prompt_b, chosen, tag)
            save_liked_prompt_to_rag(task, selected_prompt, tag)
            print("Preferred prompt saved.")

        else:
            prompt = generate_prompt_with_liked_prompt_rag(task)
            print("\nSuggested Prompt:\n")
            print(prompt)

            tried = input("\nDid you try this prompt in ChatGPT or another tool? (y/n): ").strip().lower()
            if tried == "y":
                feedback = collect_feedback()
                score = score_prompt(prompt, task)
                print("\nLLM Score for this prompt:\n")
                print(score)

                save_prompt(task, prompt, feedback, tag)
                if feedback.lower().startswith("yes") or "👍" in feedback:
                    save_liked_prompt_to_rag(task, prompt, tag)
                    print("Prompt saved for future context.")
            else:
                print("Try the prompt, then return to rate it.\n")

        print("\n---\n")

if __name__ == "__main__":
    start_prompt_assistant()