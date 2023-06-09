from .proxy_utils import reset_ip
from .config import openAIClient 

from log import Log, Feature

log = Log("chatgpt", Feature.Command)

async def chatCompletion(prompt:str):
    try:
        log.info(f"Generating chat completion... with prompt: {prompt}")
        response = openAIClient.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ],
        )
        chat_completion_message = response["choices"][0]["message"]["content"]
        log.info(f"Chat completion: {chat_completion_message}")
    
        return chat_completion_message 

    except Exception as e:
        if "authorized ip address" in e.args[0].lower():
            await reset_ip()
            return await chatCompletion(prompt)