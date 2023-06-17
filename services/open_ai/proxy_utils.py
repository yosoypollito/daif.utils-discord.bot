import requests

from decouple import config

from utils import fake_useragent

api_key = config("OPEN_AI_API_KEY")
proxy_host = config("OPEN_AI_PROXY_HOST")
async def reset_ip():
    print("Reseting proxy ip address...")
    
    print(api_key, proxy_host)
    
    headers = {
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json",
      "User-Agent": fake_useragent
    }
    
    try:
        response = requests.post(f"{proxy_host}/resetip", headers=headers)
    except Exception as e:
        print("Error resetting proxy ip address")
        return False
    
    print("Done!")
    
    return True