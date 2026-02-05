import requests

from config import TOKEN


BASE_URL = F'https://api.telegram.org/bot{TOKEN}'

def get_me() -> dict:
    get_url = f'{BASE_URL}/getMe'
    
    response = requests.get(get_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Telegram server xatolik qaytardi!')

print(get_me())