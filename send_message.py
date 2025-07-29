import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

params = {
    'chat_id': 7869144669,
    'text': "Assalomu Aleykum!"
}

r = requests.get(url=url, params=params)

print(r.status_code)
