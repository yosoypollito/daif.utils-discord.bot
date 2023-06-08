import requests
from decouple import config

url = config("MICROSOFT_TRANSLATE_URL")
token = config("MICROSOFT_TRANSLATE_API_KEY")

async def translate(from_:str, to:str, text:str):
    
    headers = {
        "Content-Type":"application/json",
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(f"{url}?from={from_}&to={to}&text={text}", headers=headers)

    response_json = response.json()
    
    return response_json