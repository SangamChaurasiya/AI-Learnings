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
model = "qwen/qwen3.8-27b"

JD = """
We are hiring a Backend Python Developer.

Requirements:
    - Strong Python
    - FastAPI or Django
    - PostgreSQL
    - Docker
    - AWS
    - REST APIs
    - 2+ years of experience
"""

RESUME = """
Name: Rahul Sharma
Experience: 3 years as a Software Developer
Skills: Python, FastAPI, MySQL, Docker, REST APIs, Git
Projects: Built a food delivery backend using the FastAPI and MySQL. Deployed application using Docker.
"""

def ask_llm(system_prompt, user_prompt):
    sys_msg = {
        "role": "system",
        "content": system_prompt
    }

    user_msg = {
        "role": "user",
        "content": user_prompt
    }

    messages = [sys_msg, user_msg]

    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content

    return answer


def step1_resume_extract():
    system_prompt = """
        You are a professional HR assistant. Extract the skills from the candidate resume provided. Only return the skills no other information. Do not invent any skills by yourself.
    """

    user_prompt = f"""
        Extract the skills from this resume {RESUME}.
    """

    return ask_llm(system_prompt, user_prompt)


def step2_jd_extract():
    system_prompt = """
        You are a professional HR assistant. Extract the skills from the JD provided. Only return the skills no other information. Do not invent any skills by yourself.
    """

    user_prompt = f"""
        Extract the skills from this JD {JD}.
    """

    return ask_llm(system_prompt, user_prompt)


def step3_match(candiate, jd):
    system_prompt = """
        You are a professional HR assistant. Compare the skills of candidate and the skills required in JD and produce a final score between 1 and 100. Also produce a sort verdict whether the candidate is a good fit for the role.
    """

    user_prompt = f"""
        Compare and match the skills of JD: {jd} and Candidate: {candidate}
    """

    return ask_llm(system_prompt, user_prompt)


candidate = step1_resume_extract()
sleep(2)
jd = step2_jd_extract()
sleep(2)
score = step3_match(candidate, jd)
sleep(2)
print(score)
