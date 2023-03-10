import openai
import os
import random
import time
import re
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('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')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop=None,
        timeout=10,
    )
    message = response.choices[0].text
    return message

while True:
    prompt = input("You: ")
    response = generate_response(prompt)
    print("Bot:", response)
    time.sleep(1)