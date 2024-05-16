import requests
from .models import TeleSettings

# token та chat_id берете для вашого бота
token = '7086418065:AAGX88t6rrEkYSG38L2H2qqWtUnlvaY33kk'
chat_id = '-4204410975'
text = 'New text'


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]
            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slise = text
        try:
            req = requests.post(method, data={ 'chat_id': chat_id, 'text': text_slise })
        except:
            pass
        finally:
            if req.status_code !=200:
                print("Помилка відправлення")
            elif req.status_code == 500:
                print("Помилка 500")
            else: print("Все Ок, повідомлення відправлене!")
    else:
        pass

# def sendTelegram(tg_name, tg_phone):
#     settings = TeleSettings.objects.get(pk=1)
#     token = str(settings.tg_token)
#     chat_id = str(settings.tg_chat)
#     text = str(settings.tg_message)
#     api = 'https://api.telegram.org/bot'
#     method = api + token + '/sendMessage'
#     part_1 = text[0: text.find('{')]
#     part_2 = text[text.find('}') + 1:text.rfind('{')]
#     part_3 = text[text.rfind('}'):-1]
#     text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
#     req = requests.post(method, data={'chat_id': chat_id, 'text': text_slise})


sendTelegram('tg_name', 'tg_phone')
