import openai

from decouple import config
api_key = config("OPEN_AI_API_KEY")
api_base = config("OPEN_AI_API_BASE")

def load_openai():
  print("Loading openai config")

  openai.api_key = api_key
  openai.api_base = api_base


async def setup():
    print("Loading openai")