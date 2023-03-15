import sqlite3

import requests
import json
import random
'''
#s- поиск по жанру, t - по тайтлу
url_for_movies = 'http://www.omdbapi.com/?apikey=8344471a&s='
keywords = ['action', 'comedy', 'thriller', 'romantic', 'sci-fi', 'horror', 'adventure', 'crime', 'animation']

pages = list(range(1,100))
random_page = random.choice(pages)
random_keyword = random.choice(keywords)

#print(random_keyword)

try: 
    response = requests.get(url_for_movies + random_keyword + '&page=' + random_page)
    response.raise_for_status() # проверяется статус ответа (если не 200-299, то пробрасывается в ошибку)
    data = response.json()
    if data['Response'] == 'True':
        movies = data['Search']
        print(movies)
        random_movie = random.choice(movies)

        movie_id = random_movie['imdbID']
        url = 'http://www.omdbapi.com/?apikey=8344471a&i=' + movie_id
        response = requests.get(url)
        response.raise_for_status()
        random_movie_details = response.json()
        #print(random_movie_details)
    else:
        print('Введите фильм')
except requests.exceptions.HTTPError as error:
    print('Ошибочка'.format(error))

except requests.exceptions.ConnectionError as error:
    print('Ошибка при соединении'.format(error))
'''
r = round(random.uniform(7.4, 10.0), 1)
print(r)

w = random.randint(1, 3)
print(w)

data = [
    ("Куртка", "Зима", -30, 0, ["https://kosmo-shop.com/25192/kurtka-raduzhnaya-get-rainbow-mood-raduga-mnogocvetnaya-yarkaya-prikolnaya-veselaya.jpg", "https://framen.ru/d/kurtka-dlinnaja-s-klimat-kontrolem-761-autojack.jpg?h=800", "https://ae01.alicdn.com/kf/H7a65d3f8bf0c4404baf93aa59170366aE.jpg", "https://ae04.alicdn.com/kf/S2ba24b1e2df1447c9b7f5ad891b6834ee.jpg_640x640.jpg"]),
    ("Штаны", "Зима", -30, 0, ["https://kasta.ua/image/1035/s3/5/36/15/9735189/27884299/27884299_original.jpeg"]),
    ("Аксессуар", "Зима", -30, 0, ["https://darvin-market.ru/upload/iblock/0f1/0f1afae5dd8a87086eb74a4fd5494546.jpeg"]),
    ("Футболка", "Зима", -30, 0, ["https://printbar.ru/upload/images/0b/0bb7483.jpg", "https://printbang.ru/img/products/85/muzhskaya-futbolka-pepe-fon-rikardo-milos-fleksonskiy-85979.jpg", "https://bukva-z.ru/upload/thumb/images/go/goh2c1zj0f4_590x0.jpg", "https://printbar.ru/upload/images/mp/mpvtuxi.jpg"])
]

for item in data:
    name, season, temp_min, temp_max, urls = item
    print(urls)