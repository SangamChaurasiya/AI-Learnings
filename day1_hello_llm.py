import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Get the Groq API Key
my_api_key = os.getenv('GROQ_API_KEY')

if not my_api_key:
    raise ValueError("API KEY Error")

# Set Client related information like model, role, prompt etc.
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-safeguard-20b"
role = "user"
prompt = "Who is Virat Kohli?"
message = {
    "role": role,
    "content": prompt
}

messages = [message]
response = client.chat.completions.create(
    model=model,
    messages=messages
)

# Get the response
answer = response.choices[0].message.content

print(answer)

# uv venv --python 3.12
# uv add groq python-dotenv
