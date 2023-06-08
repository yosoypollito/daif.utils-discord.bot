from .proxy_utils import reset_ip

import openai
from decouple import config

api_key = config("OPEN_AI_API_KEY")
api_base = config("OPEN_AI_API_BASE")

openai.api_key = api_key
openai.api_base = api_base

async def chatCompletion(prompt:str):
    try:
        print(f"Generating chat completion... with prompt: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ],
        )
        chat_completion_message = response["choices"][0]["message"]["content"]
        print(f"Chat completion: {chat_completion_message}")
    
        return chat_completion_message 

    except Exception as e:
        if "authorized ip address" in e.args[0].lower():
            await reset_ip()
            return await chatCompletion(prompt)