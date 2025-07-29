from pprint import pprint
import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

params = {

    'chat_id': 7869144669,
    'photo' : 'https://images.app.goo.gl/xm3R3g161ATEYRwo9'


}

r = requests.get(url=url , params=params)

print(r.status_code)
pprint(r.json())