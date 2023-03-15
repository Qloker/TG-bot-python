import requests
import json


url = 'https://api.mymemory.translated.net/get'


def translate_text(text, from_lang, to_lang):
    params = {'q': text, 'langpair': f'{from_lang}|{to_lang}'}
    #print(text)
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        translated_text = data['responseData']['translatedText']
        return translated_text
    else:
        return text


test = translate_text('few clouds', 'en', 'ru')
#print(test)