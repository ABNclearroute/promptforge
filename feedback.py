from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


client = OpenAI(
    api_key=os.getenv("HALO_API_KEY"),
    base_url=os.getenv("base_url")
)

def collect_feedback():
    rating = input("Was the output helpful? (yes/no or 👍/👎): ").strip()
    notes = input("Any comments (optional): ").strip()
    return f"{rating} | {notes}"

def score_prompt(prompt, user_goal):
    response = client.chat.completions.create(
        model="google/gemini-2.5-flash-preview-05-20",
        messages=[
            {"role": "system", "content": "You are a helpful prompt engineer. Score the following prompt for clarity, tone, and alignment with the user's task."},
            {"role": "user", "content": f"User Task: {user_goal}\n\nPrompt: {prompt}\n\nScore and give a short reason."}
        ]
    )
    return response.choices[0].message.content