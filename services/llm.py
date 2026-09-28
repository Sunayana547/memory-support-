import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

MODEL = "openai/gpt-oss-120b"


def generate_response(customer_message, memories):
    memory_text = "\n".join(
        f"- {memory.text}"
        for memory in memories
    )

    prompt = f"""
You are a professional customer support AI agent.

Your job is to help customers solve their problems.

CURRENT CUSTOMER MESSAGE:
{customer_message}

RELEVANT CUSTOMER MEMORY:
{memory_text}

Instructions:
1. Use the previous memory when it is relevant.
2. Do not invent customer history.
3. Do not mention Hindsight or internal memory systems to the customer.
4. Give a clear, helpful and personalized response.
5. If previous troubleshooting worked before, consider it when responding.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful customer support agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content