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

# User Requirements Here
message = {
    "role": "user",
    # "content": "I love you baby!"
    "content": "Suggest a name for my cloth company"
}

# Behaviour gets decided based on the content of the system
message_system = {
    "role": "system",
    # "content": "You are my loving girlfriend"
    # "content": "You are my strict office colleague who is also my manager"
    "content": "You are a brand manager who suggests name for my company. Name should be in one word. Suggest one name only"
}
messages = [message_system, message]

# Temperature by default 0 meaning safe
response = client.chat.completions.create(model=model, messages=messages, temperature=1)

answer = response.choices[0].message.content

print(answer)

# uv venv --python 3.12
# uv add groq python-dotenv
