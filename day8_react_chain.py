import os
import re
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

def get_product_price(product):
    if product == 'iPhone 17':
        return 1000
    elif product == 'iPhone 15':
        return 500 
    else:
        return 0
    
def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Calc Error!"
    
tools = {
    "get_product_price": get_product_price,
    "calculator": calculator
}

system_prompt = """
You are a shopping assistant.

You have these tools:
get_product_price(product)
calculator(expression)

IMPORTANT:
Call tools ecactly like these examples:

Action: get_product_price("iPhone 17")
Action: calculator("5000 - 1000")

Never Write:
get_product_price(product="iPhone 17")

Never Write:
calculator("5000 - 1000")

Follow these rules:
1. Decide what you need to do next.
2. Call ONLY ONE tool at a time.
3. After writing an Action, STOP immediately.
4. Never guess or invent a tool result.
5. Wait until you receive an observation.
6. Then decide your next action.
7. When the task is complete, give the final answer.

Format:
Thought: what you need to do
Action: tool_name(argument)

When Finished:
Final Answer: your answer
"""

def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):
        print("\n----------------")
        print(f"Step{step + 1}")
        print("----------------")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )

        answer = response.choices[0].message.content

        print(answer)

        # Agent has finished
        if "Final Answer:" in answer:
            break

        # Find the action
        match = re.search(r"Action: \s*(\w+)\((.*?)\)", answer)

        if match:
            tool_name = match.group(1)
            tool_input = match.group(2)
            tool_input = tool_input.strip()
            tool_input = tool_input.strip('"')

            # Run the tool
            if tool_name in tools:
                tool = tools[tool_name]
                observation = tool(tool_input)
            else:
                observation = "Tool not found"

            print("Observation: ", observation)

            # Add LLM response to memory
            messages.append({
                "role": "assistant",
                "content": answer
            })
            
            # Give tool result back to LLM
            messages.append({
                "role": "user",
                "content": f"Observation: {observation}"
            })
            sleep(5)

prompt = """
I have 5000 rupees. What is the price of an iPhone 17? and how much money will I have left with?
"""

run_agent(prompt)
