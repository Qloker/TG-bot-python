

import requests
import json
import random

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

