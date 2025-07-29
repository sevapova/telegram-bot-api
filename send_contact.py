from pprint import pprint
import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/sendContact'

params = {

    'chat_id': 7869144669,
    'phone_number': '+998906002307',
    'first_name': 'Sevara',
    'last_name': 'Latipova'
}

r = requests.get(url=url, params=params)

print(r.status_code)
pprint(r.json())
