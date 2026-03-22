from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(messages):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {type(e).__name__} - {e}"