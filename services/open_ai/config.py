import openai

from decouple import config
api_key = config("OPEN_AI_API_KEY")
api_base = config("OPEN_AI_API_BASE")

class OpenAIClient():
  def __init__(self):
    self.openai = openai
    
    self.openai.api_key = api_key
    self.openai.api_base = api_base
    
    self.ChatCompletion = self.openai.ChatCompletion 
    self.Completion = self.openai.Completion
    self.Image = self.openai.Image