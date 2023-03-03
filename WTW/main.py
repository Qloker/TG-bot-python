import telebot
import requests
import random
from telebot import types
#from telebot import types

token = '6076273456:AAFuxoL1xd9gxkEKDo1bfwgVieNZumSxSNA'
bot = telebot.TeleBot(token)

API_KEY = '1d442f5e38536b0955c89d1f7fd0f83c'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

def translate_text(text, from_lang, to_lang):
    url = 'https://api.mymemory.translated.net/get'
    params = {'q': text, 'langpair': f'{from_lang}|{to_lang}'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        translated_text = data['responseData']['translatedText']
        return translated_text
    else:
        return None


#функция получения погоды
def get_weather(lat, lon):
    params = {'lat': lat, 'lon': lon, 'appid': API_KEY}
    response = requests.get(WEATHER_URL, params = params)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        print(data)
        temperature = data['main']['temp'] - 273.15
        translated_desc = translate_text(weather_desc, 'en', 'ru')
        return translated_desc, temperature
       # return data['weather'][0]['description'], data['main']['temp'] - 273.15
    else:
        return None, None


#Создание клавиатуры
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

buttons = [
    types.KeyboardButton('Геолокация', request_location=True),
    types.KeyboardButton('Что это?'),
    types.KeyboardButton('Заролить фильмец'),
    types.KeyboardButton('Что-то еще11'),
    types.KeyboardButton('Что-то еще123'),
    types.KeyboardButton('🤡')
]

'''
button1 = telebot.types.KeyboardButton('Поделиться геолокацией', request_location = True)
button2 = telebot.types.KeyboardButton('Нажми тут')
button3 = telebot.types.KeyboardButton('ЖЖП')
'''

keyboard.add(*buttons)

chat_id = 0

#Обработка команд
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Давай поможем тебе выбрать че надеть.\nДля этого мне потребуется твоя геолокация, чтобы я мог глянуть погоду и подсказать', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Im here to help u', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'Что это?':
        bot.send_message(message.chat.id, 'Пока похуй', reply_markup=keyboard)
    elif message.text == 'Заролить фильмец':
        answer = ''
        url_for_movies = 'http://www.omdbapi.com/?apikey=8344471a&s='
        keywords = ['action', 'comedy', 'thriller', 'romantic', 'sci-fi', 'horror', 'adventure', 'crime', 'animation']
        random_keyword = random.choice(keywords)
        pages = list(range(1,3))
        random_page = random.choice(pages)
        try: 
            response = requests.get(url_for_movies + random_keyword + '&page=' + str(random_page))
            response.raise_for_status() # проверяется статус ответа (если не 200-299, то пробрасывается в ошибку)
            data = response.json()
            if data['Response'] == 'True':
                movies = data['Search']
                random_movie = random.choice(movies)

                movie_id = random_movie['imdbID']
                url = 'http://www.omdbapi.com/?apikey=8344471a&i=' + movie_id
                response = requests.get(url)
                response.raise_for_status()
                random_movie_details = response.json()
                print(random_movie_details)
                answer = random_movie_details['Title']

                photo_url = random_movie_details['Poster']
                if photo_url != 'N/A':
                    photo_response = requests.get(photo_url)
                    print(photo_url)
                    if photo_response.status_code == 200:
                        photo = photo_response.content
                        bot.send_photo(chat_id=message.chat.id, photo=photo)
                else:
                    print('Тут без фото')
    

            else:
                answer = 'Введите фильм'
                print('Введите фильм')
        except requests.exceptions.HTTPError as error:
             print('Ошибочка'.format(error))

        except requests.exceptions.ConnectionError as error:
             print('Ошибка при соединении'.format(error))
        bot.send_message(message.chat.id, answer, reply_markup=keyboard)

    elif message.text == 'Что-то еще11':
        bot.send_message(message.chat.id, 'Жора Жирный Педик', reply_markup=keyboard)
    elif message.text == 'Что-то еще123':
        bot.send_message(message.chat.id, 'Жора Жирный Педик', reply_markup=keyboard)
    elif message.text == '🤡':
        bot.send_message(message.chat.id, 'Наконец то ты нажал на себя', reply_markup=keyboard)
    else:
         bot.send_message(message.chat.id, 'Тыкни в кнопку, а не пиши в чат', reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def share_geo(message):
    lat, lon = message.location.latitude, message.location.longitude
    print(lat, lon)
    description, temperature = get_weather(lat, lon)
    if description and temperature:
        response_text = f'Сейчас на улице {description}, температура {temperature:.1f} градусов'
    else:
        response_text = 'Че то не получилось'
    bot.send_message(message.chat.id, response_text)

'''

@bot.message_handler(commands=['Нажми тут'])
def command2(message):
    bot.send_message(message.chat.id, 'Пs, пока не сделано')
    
@bot.message_handler(commands=['ЖЖП'])
def command3(message):
    bot.send_message(message.chat.id, 'Жоs sd')
'''
bot.polling(none_stop=True)

