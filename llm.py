import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def analyze_notice(text):

    prompt = f"""
Analyze this notice and provide:

📌 Summary
📅 Important Dates
ℹ️ Important Information
✅ Actions Required
⏰ Deadline

Notice:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content