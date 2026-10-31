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

# Step1 - Knowledge Base
knowledge_base = {
    "age": "The age of Pratyush is 25 years.",
    "net worth": "The net worth of Pratyush is 2000."
}

# Step2 - Retrieval
def retrieve_info(question):
    question = question.lower()

    if "age" in question:
        return knowledge_base["age"]
    elif "net worth" in question:
        return knowledge_base["net worth"]
    else:
        return None
    

def ask_llm(question):
    context = retrieve_info(question)

    sys_prompt = f"Answer in one line only. Answer only based on this context. Do not hallucinate. Context: {context}"
    sys_message = {
        "role": "system",
        "content": sys_prompt
    }

    message = {
        "role": "user",
        "content": question
    }

    messages = [sys_message, message]

    response = client.chat.completions.create(model=model, messages=messages)

    answer = response.choices[0].message.content

    return answer


question = "Do you know father name of Pratyush?"
print(ask_llm(question))
