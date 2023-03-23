import telebot
import requests
import random
from telebot import types
import Services.getMovie
import Services.getWeather
import Services.translateText
import Services.getClothes
import Services.getJoke

get_film = Services.getMovie

#from telebot import types

#бот телеги и его токен
token = '6076273456:AAFuxoL1xd9gxkEKDo1bfwgVieNZumSxSNA'
bot = telebot.TeleBot(token)

#Создание клавиатуры
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_for_films = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

buttons = [
    types.KeyboardButton('Что надеть сегодня?', request_location=True),
    types.KeyboardButton('Что это?'),
    types.KeyboardButton('Заролить фильмец'),
    types.KeyboardButton('Выбрать фильмец'),
    types.KeyboardButton('Анекдот'),
    types.KeyboardButton('🤡')
]

buttons_for_films = [
    types.KeyboardButton('Комедия'),
    types.KeyboardButton('Триллер'),
    types.KeyboardButton('Драма'),
    types.KeyboardButton('Аниме'),
    types.KeyboardButton('Детектив'),
    types.KeyboardButton('Заролить фильм'),
    types.KeyboardButton('Меню 📱')
]
buttons_pressed = 0

keyboard.add(*buttons)

keyboard_for_films.add(*buttons_for_films)

#Обработка команд
@bot.message_handler(commands=['start'])
def start(message):
    global buttons_pressed
    buttons_pressed = buttons_pressed + 1
    print(buttons_pressed)
    text_answer = 'Давай поможем тебе выбрать че надеть.\nДля этого мне потребуется твоя геолокация, чтобы я мог глянуть погоду и подсказать\nВообще я тут все подряд решил тестить так что воооот'
    bot.send_message(message.chat.id, text_answer, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Im here to help u', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    global buttons_pressed
    buttons_pressed = buttons_pressed + 1
    print(buttons_pressed)

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
        print(film)
        photo = get_film.get_image(film['image'])
        if photo == 'Без фото':
            print('ERROR')
        else:
            bot.send_photo(chat_id=message.chat.id, photo=photo)

        if film['desc'] == 'None':
            bot.send_message(message.chat.id, film['name'], reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, film['name'], reply_markup=keyboard)
            bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard)
            

    elif message.text == 'Анекдот':
        joke = Services.getJoke.random_joke()
        bot.send_message(message.chat.id, joke, reply_markup=keyboard)
        
    elif message.text == '🤡':
        bot.send_message(message.chat.id, 'Наконец то ты нажал на себя', reply_markup=keyboard)


    elif message.text == 'Выбрать фильмец':
        text = 'Выбери жанр, который хочешь посмотреть или зарандомь'
        bot.send_message(message.chat.id, text=text, reply_markup=keyboard_for_films)
    
   
    # Жанры фильмов
    elif message.text == 'Комедия':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец')
       
        film = Services.getMovie.search_with_genre(message.text.lower())
        photo = get_film.get_image(film['img_url'])
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        bot.send_message(message.chat.id, film['name'], reply_markup=keyboard_for_films)
        bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard_for_films)

    elif message.text == 'Триллер':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец')
       
        film = Services.getMovie.search_with_genre(message.text.lower())
        photo = get_film.get_image(film['img_url'])
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        bot.send_message(message.chat.id, film['name'], reply_markup=keyboard_for_films)
        bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard_for_films)

    elif message.text == 'Драма':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец')
       
        film = Services.getMovie.search_with_genre(message.text.lower())
        photo = get_film.get_image(film['img_url'])
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        bot.send_message(message.chat.id, film['name'], reply_markup=keyboard_for_films)
        bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard_for_films)

    elif message.text == 'Аниме':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец')
       
        film = Services.getMovie.search_with_genre(message.text.lower())
        photo = get_film.get_image(film['img_url'])
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        bot.send_message(message.chat.id, film['name'], reply_markup=keyboard_for_films)
        bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard_for_films)

    elif message.text == 'Детектив':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец')
       
        film = Services.getMovie.search_with_genre(message.text.lower())
        photo = get_film.get_image(film['img_url'])
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        bot.send_message(message.chat.id, film['name'], reply_markup=keyboard_for_films)
        bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard_for_films)

    elif message.text == 'Заролить фильм':
        bot.send_message(message.chat.id, 'Секундочку, уже ищу для тебя фильмец', reply_markup=keyboard)

        film = Services.getMovie.random_movie_search()
        photo = get_film.get_image(film['image'])
        bot.send_photo(chat_id=message.chat.id, photo=photo)
        bot.send_message(message.chat.id, film['name'], reply_markup=keyboard_for_films)
        bot.send_message(message.chat.id, film['desc'], reply_markup=keyboard_for_films)



    elif message.text == 'Меню 📱':
        bot.send_message(message.chat.id, 'Возврат в меню', reply_markup=keyboard)
    #else:
        # bot.send_message(message.chat.id, 'Тыкни в кнопку, а не пиши в чат', reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def share_geo(message):
    global buttons_pressed
    buttons_pressed = buttons_pressed + 1
    print(buttons_pressed)

    lat, lon = message.location.latitude, message.location.longitude     #получение широты и долгоы от бота
    weather = Services.getWeather.get_weather(lat, lon)                  #получение погоды через функция запроса (вынесена)
    description, temperature = weather
    desc = Services.translateText.translate_text(description, 'en','ru')

    # не равно 1, потому что если будет беда с запросом, то функция вернет 1 1
    if description != 1 and temperature != 1:
        response_text = f'Сейчас на улице {desc}, температура {temperature:.1f} градусов\nДавай подберем тебе одежду'
    else:
        response_text = 'Че то не получилось. Возможно, не удалось получить данные о геолокации'

    bot.send_message(message.chat.id, response_text, reply_markup=keyboard)

    clothes = Services.getClothes.get_clothing_by_temp(round(temperature))
    cloth = []
    img_clothes = []

    #Получение случайной вещи (ссылки) из массива с ссылками
    for i in range(0, len(clothes)):
        c = clothes[i][1][random.randint(0, ((len(clothes[i][1]) - 1)))]
        cloth.append(clothes[i][1][random.randint(0, ((len(clothes[i][1]) - 1)))])
        img = Services.getMovie.get_image(c)
        bot.send_photo(chat_id=message.chat.id, photo=img)

    #Получение картинки из массива
    #for i in range(0, len(cloth)):
      #  img_clothes.append(Services.getMovie.get_image(cloth[i]))

    #отправка ботом картинки в чат
   # for i in cloth:
     #   bot.send_photo(chat_id=message.chat.id, photo=i)

    bot.send_message(message.chat.id, 'Поздравляю, теперь вы одеты как черт, носи с удовольствием')



bot.polling(none_stop=True)

