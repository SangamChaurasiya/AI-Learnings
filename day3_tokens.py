import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')

if not my_api_key:
    raise ValueError("API KEY Error")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-safeguard-20b"

role = "user"
prompt1 = "Hi!"
prompt2 = "Explain time travel in detail"
prompt3 = "Write a 1000 word essay on Machine Learning"

prompts = [prompt1, prompt2, prompt3]

messages = []

for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }
    messages = [message]
    # response = client.chat.completions.create(model=model, messages=messages)
    
    # Limiting the tokens
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)

    usage = response.usage

    print("Prompt - ", prompt)
    print("Input Tokens - ", usage.prompt_tokens)
    print("Output Tokens - ", usage.completion_tokens)
    print("Total Tokens - ", usage.prompt_tokens + usage.completion_tokens)
    print("Finish Reason - ", response.choices[0].finish_reason)
    print(("=" * 100) + "\n")

# uv venv --python 3.12
# uv add groq python-dotenv
