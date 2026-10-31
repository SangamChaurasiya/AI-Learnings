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

from pydantic import BaseModel

# Pydantic Model for getting the required data only
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

# Creatign the schema
schema = Ticket.model_json_schema()

# Setting the response format as JSON
response_format = {
    "type": "json_object"
}

# Set the system prompt and make sure it has json keyword in it for sending the output in the JSON format.
system_prompt = f"""
    Extract the personal information from the ticket strictly based on this schema {schema} and give me a json output.
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

text = "Hello, my name is Sangam. I have an iPhone which is not working at all. My address is varanasi. My email is abc@gmail.com. My contact is 63067. "
prompt = f'''
    This is the customer ticket. Please extract the personal information provided to me from this "{text} of this schema {schema}".
'''
message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

answer = response.choices[0].message.content

print(answer)

# Reading the JSON output
import json

raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)


# uv venv --python 3.12
# uv add groq python-dotenv
# uv add pydantic
