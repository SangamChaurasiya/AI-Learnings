import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2") # 384

load_dotenv()

# Get the Groq API Key
my_api_key = os.getenv('GROQ_API_KEY')

if not my_api_key:
    raise ValueError("API KEY Error")

# Set Client related information like model, role, prompt etc.
client = Groq(api_key=my_api_key)
groqmodel = "openai/gpt-oss-safeguard-20b"

documents = [
    "Employees receive 24 days of paid leave per year.",

    "Employees work from the office on Tuesday, Wednesday and Thursday."
    "Monday and Friday are optional work-from-home days.",

    "Employees receive Rs 3000 per month for gym reimbursment.",

    "Employees can claim Rs 2000 per month for home internet.",

    "Employee have a 90 day notice period."
]

document_embedding = model.encode(documents)


def cosine_similarity(a, b):
    return np.dot(a, b) / ( np.linalg.norm(a) * np.linalg.norm(b) ) 


def retrieve(qembedding):
    scores = []
    for i, document in enumerate(document_embedding):
        score = cosine_similarity(qembedding, document)
        scores.append((score, documents[i]))

    scores.sort(reverse=True)

    return scores[0]



def ask_llm(question, context):
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

    response = client.chat.completions.create(model=groqmodel, messages=messages)

    answer = response.choices[0].message.content

    return answer


query = "How much vacation do I get?"
qembedding = model.encode(query)

score, context = retrieve(qembedding)

answer = ask_llm(query, context)
print(answer)
