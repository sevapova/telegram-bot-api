from pprint import pprint
import requests
from settings import TOKEN


url = f'https://api.telegram.org/bot{TOKEN}/sendVoice'

params = {
    
    'chat_id': 7869144669,
    'voice': 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Example.ogg'

}

r = requests.get(url=url, params=params)
print(r.status_code)
pprint(r.json())