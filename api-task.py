import time
import os
import requests
import telegram
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

token_vk = os.getenv('token_vk')
account_sid = os.getenv('Sid')
auth_token = os.getenv('Token') #токен twilio


TELEGRAM_TOKEN = os.getenv('tg_token')  # добавить токен тг
CHAT_ID = os.getenv('chat_id')# chat_id бота


def get_status(user_id):
    params = {
        'access_token': token_vk,
        'v': '5.92',
        'fields': 'online',
        'user_id': user_id
    }
    result = requests.post('https://api.vk.com/method/users.get', data = params).json()['response']
    return result[0]['online'] #проверка пользователя online


# def sms_sender(sms_text): #отправка sms через Twillo 
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(body=sms_text, from_='+12569077950', to='+79083013855')
#     return message.sid # sid cообщения


def sms_sender(message): #отправка статуса телеграмм боту
    tg = telegram.Bot(token=TELEGRAM_TOKEN) #request=proxy
    send = tg.send_message(chat_id=CHAT_ID, text=message)
    return send


# if __name__ == "__main__":
#     vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        print('Не в сети')
        time.sleep(5)
