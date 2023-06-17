import openai
import urllib.request as requests

from .proxy_utils import reset_ip

from .config import openAIClient 
from log import Log, Feature

from utils import fake_useragent

log = Log("dall_e", Feature.Command)

async def generateImage(prompt):
  log.info("Generating image")
  try:
    response = openAIClient.Image.create(prompt=prompt, n=1, size="1024x1024")
  except Exception as e:
    print("error", e.args)
    if "authorized ip address" in e.args[0].lower():
      await reset_ip()
      return await generateImage(prompt)
  
  log.info("Image created")
  
  img_url = response["data"][0]["url"]
  
  r = requests.Request(img_url, headers={'User-Agent': fake_useragent})
  f = requests.urlopen(r)
  
  return f.read()