

import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt, model="gpt-3.5-turbo", temperature=0.7):
    """
    Send a prompt to the LLM and return its response.
    """
    try:
        print(f"[LLM] Prompt: {prompt}")
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for elderly care."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=150
        )
        answer = response['choices'][0]['message']['content'].strip()
        print(f"[LLM] Response: {answer}")
        return answer

    except Exception as e:
        print(f" Error calling LLM: {e}")
        return "Sorry, I couldn't understand. Please try again."

# Test run
if __name__ == "__main__":
    reply = ask_llm("What are some health tips for elderly people?")
    print("LLM says:", reply)
