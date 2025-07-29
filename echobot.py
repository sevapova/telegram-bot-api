import time
import requests
from settings import TOKEN

url_get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
url_send_message = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

try:
    with open('last_update.txt', 'r') as f:
        last_update_id = int(f.read())
except FileNotFoundError:
    last_update_id = 0

while True:
    params = {
        'offset': last_update_id + 1
    }

    r = requests.get(url_get_updates, params=params)
    data = r.json()
    print(data)

    result = data.get('result', [])

    for update in result:
        msg = update.get('message', {})
        user = msg.get('from', {})
        text = msg.get('text', '')
        chat_id = user.get('id')

        if not chat_id or not text:
            continue

        if text == '/start':
            params = {
                'chat_id': chat_id,
                'text': 'salom echo botga xush kelibsiz\nbu bot text yozsangiz echo qiladi.'
            }
        else:
            params = {
                'chat_id': chat_id,
                'text': text
            }

        requests.get(url=url_send_message, params=params)

        last_update_id = update['update_id']
        with open('last_update.txt', 'w') as f:
            f.write(f'{last_update_id}')

    time.sleep(1)
