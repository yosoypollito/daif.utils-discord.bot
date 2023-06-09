import openai
import urllib.request as requests

from .config import openAIClient 
from log import Log, Feature

log = Log("dall_e", Feature.Command)

async def generateImage(prompt):
  log.info("Generating image")
  response = openAIClient.Image.create(prompt=prompt, n=1, size="1024x1024")
  
  log.info("Image created")
  
  img_url = response["data"][0]["url"]
  
  fake_useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
  r = requests.Request(img_url, headers={'User-Agent': fake_useragent})
  f = requests.urlopen(r)
  
  return f.read()