import telebot
import requests
import random
from telebot import types
import Services.getMovie
import Services.getWeather
import Services.translateText

get_film = Services.getMovie
#from telebot import types

#бот телеги и его токен
token = '6076273456:AAFuxoL1xd9gxkEKDo1bfwgVieNZumSxSNA'
bot = telebot.TeleBot(token)

#Создание клавиатуры
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_for_films = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

buttons = [
    types.KeyboardButton('Геолокация', request_location=True),
    types.KeyboardButton('Что это?'),
    types.KeyboardButton('Заролить фильмец'),
    types.KeyboardButton('Выбор жанра'),
    types.KeyboardButton('Что-то еще123'),
    types.KeyboardButton('🤡')
]

buttons_for_films = [
    types.KeyboardButton('Комедия'),
    types.KeyboardButton('Триллер'),
    types.KeyboardButton('Драма'),
    types.KeyboardButton('Аниме'),
    types.KeyboardButton('Блокбастер'),
    types.KeyboardButton('Мне повезет 🤡'),
    types.KeyboardButton('Меню 📱')
]

keyboard.add(*buttons)

keyboard_for_films.add(*buttons_for_films)

#Обработка команд
@bot.message_handler(commands=['start'])
def start(message):
    text_answer = 'Давай поможем тебе выбрать че надеть.\nДля этого мне потребуется твоя геолокация, чтобы я мог глянуть погоду и подсказать\nВообще я тут все подряд решил тестить так что воооот'
    bot.send_message(message.chat.id, text_answer, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Im here to help u', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    # Кнопка Что это
    if message.text == 'Что это?':
        text_answer = '''Пилю ботиса
Сейчас есть запрос геолокации -> получение погоды на английском -> перевод и выдача ботом описания и градусы
Фильмы ролятся по рандомному запросу
В планах сделать меню с рандомным поиском после выбора жанра
        '''
        bot.send_message(message.chat.id, text_answer, reply_markup=keyboard)

    # Кнопка рандомного фильма
    elif message.text == 'Заролить фильмец':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец', reply_markup=keyboard)
        film = get_film.random_movie_search()
        photo = get_film.get_image(film['image'])
        if photo == 'Без фото':
            print('ERROR')
        else:
            bot.send_photo(chat_id=message.chat.id, photo=photo)

        if film['desk'] == 'None':
            bot.send_message(message.chat.id, film['name'], reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, film['name'], reply_markup=keyboard)
            bot.send_message(message.chat.id, film['desk'], reply_markup=keyboard)
            

    elif message.text == 'Выбор жанра':
        text = 'Выбери жанр, который хочешь посмотреть или зарандомь'
        bot.send_message(message.chat.id, text=text, reply_markup=keyboard_for_films)

    elif message.text == 'Что-то еще123':
        bot.send_message(message.chat.id, 'Жора Жирный Педик', reply_markup=keyboard)
    elif message.text == '🤡':
        bot.send_message(message.chat.id, 'Наконец то ты нажал на себя', reply_markup=keyboard)
    elif message.text == 'Меню 📱':
        bot.send_message(message.chat.id, reply_markup=keyboard)
    else:
         bot.send_message(message.chat.id, 'Тыкни в кнопку, а не пиши в чат', reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def share_geo(message):
    translate = Services.translateText
    lat, lon = message.location.latitude, message.location.longitude     #получение широты и долгоы от бота
    weather = Services.getWeather.get_weather(lat, lon)                           #получение погоды через функция запроса (вынесена)
    description, temperature = weather
    desc = Services.translateText.translate_text(description, 'en','ru')
    # не равно 1, потому что если будет беда с запросом, то функция вернет 1 1
    if description != 1 and temperature != 1:
        response_text = f'Сейчас на улице {desc}, температура {temperature:.1f} градусов'
    else:
        response_text = 'Че то не получилось. Возможно, не удалось получить данные о геолокации'
    bot.send_message(message.chat.id, response_text)

bot.polling(none_stop=True)

