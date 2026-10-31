import os
from pathlib import Path
from time import sleep
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
prompt = "Explain how internet worrks?"

message = {
    "role": "user",
    "content": prompt
}

messages = [message]

# Response without streaming
# response1 = client.chat.completions.create(model=model, messages=messages)
# print(response1)

# answer = response1.choices[0].message.content
# print(answer)

# Response with streaming
stream = client.chat.completions.create(model=model, messages=messages, stream=True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
