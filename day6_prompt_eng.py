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


def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages)

    ans = response.choices[0].message.content

    return ans

# Bad Prompt
bad_prompt = """
This is a user complaint:
My laptop is not working
Classify this.
"""

# Good Prompt
good_prompt = """
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK:
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of the three categories namely Billing, Technical, Return
#OUTPUT FORMAT
Your answer should be in the one word only, the one word should be one of the categories in given in constraints
#EXAMPLE
For instance if a user complain says he wants a refund then the category is Return
#FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
My marriage is broke
"""

print(llm_ans(good_prompt))
