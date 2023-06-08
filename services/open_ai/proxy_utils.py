import requests

from decouple import config

api_key = config("OPEN_AI_API_KEY")
proxy_host = config("OPEN_AI_PROXY_HOST")
async def reset_ip():
    print("Reseting proxy ip address...")
    
    headers = {
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json",
    }

    response = requests.post(f"{proxy_host}/resetip", headers=headers)
    
    response_json = response.json()
    print(response_json)
    
    print("Done!")
    
    return response_json