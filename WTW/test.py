

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

asd = {'docs': [{'id': 1255656, 'type': 'tv-series', 'externalId': {'kpHD': None, 'imdb': 'tt9432978'}, 'name': 'Фабрика гениев', 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'description': None, 'votes': {'kp': 22, 'imdb': 73688, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'year': 2019, 'poster': {'url': 'https://st.kp.yandex.net/images/film_big/1255656.jpg', 'previewUrl': 'https://st.kp.yandex.net/images/film_iphone/iphone360_1255656.jpg'}, 'alternativeName': 'Kota Factory', 'enName': None, 'movieLength': 45, 'names': [{'name': 'Фабрика гениев'}, {'name': 'Kota Factory'}], 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}, 'releaseYears': [{'start': 2019, 'end': None}]}, {'id': 328059, 'alternativeName': 'The Magic of David Copperfield VII: Familiares', 'description': None, 'enName': None, 'externalId': {'kpHD': None, 'imdb': 'tt0293377'}, 'movieLength': 50, 'name': None, 'names': [{'name': 'The Magic of David Copperfield VII: Familiares'}], 'poster': None, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'shortDescription': None, 'type': 'movie', 'votes': {'kp': 22, 'imdb': 23, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'year': 1985, 'logo': {'url': None}, 'watchability': {'items': None}}, {'id': 882915, 'type': 'movie', 'externalId': {'kpHD': None, 'imdb': 'tt4127676'}, 'name': None, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'description': None, 'votes': {'kp': 18, 'imdb': 78, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'year': 2014, 'poster': None, 'alternativeName': 'TSA America: Yeah, But Is It Ticking?', 'enName': None, 'movieLength': 6, 'names': [{'name': 'TSA America: Yeah, But Is It Ticking?'}], 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}}, {'id': 479716, 'type': 'movie', 'externalId': {'kpHD': None, 'imdb': 'tt1523972'}, 'name': None, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 
0, 'await': 0}, 'description': None, 'votes': {'kp': 17, 'imdb': 198, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'year': 2011, 'poster': {'url': 'https://st.kp.yandex.net/images/film_big/479716.jpg', 'previewUrl': 'https://st.kp.yandex.net/images/film_iphone/iphone360_479716.jpg'}, 
'alternativeName': "Tomorrow's End", 'enName': None, 'movieLength': 100, 'names': [{'name': "Tomorrow's End"}], 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}}, {'id': 4843920, 'names': [{'name': 'Au79'}], 'alternativeName': 'Au79', 'description': 'Валерий\xa0—\xa0пенсионер, который работает ночным сторожем в\xa0новостройке. От\xa0своего покойного дедушки в\xa0наследство он\xa0получил золото. Вскоре Валерий решает спрятать золото в\xa0заброшенном месте, подальше от\xa0членов его\xa0семьи. В\xa0этот день он\xa0даже не\xa0подозревал, что\xa0история, которая произошла с\xa0его дедом, может повториться.', 'enName': None, 'externalId': {'kpHD': None, 'imdb': 'tt16923052', 'tmdb': 1016585}, 'movieLength': 6, 'name': None, 'poster': {'url': 'https://st.kp.yandex.net/images/film_big/4843920.jpg', 'previewUrl': 'https://st.kp.yandex.net/images/film_iphone/iphone360_4843920.jpg'}, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'shortDescription': None, 'type': 'movie', 'votes': {'kp': 17, 'imdb': 6, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'year': 2022, 'logo': {'url': None}, 'watchability': {'items': None}}, {'externalId': {'kpHD': None, 'imdb': 'tt0376364'}, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 
'await': 0}, 'votes': {'kp': 16, 'imdb': 1191, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'id': 442773, 'type': 'tv-series', 'name': None, 'description': None, 'year': 2003, 'poster': None, 'alternativeName': '31 minutos', 'enName': None, 'names': [{'name': '31 minutos'}], 'movieLength': 31, 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}, 'releaseYears': [{'start': 2003, 'end': 2014}]}, {'id': 
848484, 'type': 'movie', 'externalId': {'kpHD': None, 'imdb': 'tt3835244'}, 'name': 'Снайпер Мопс', 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'description': None, 'votes': {'kp': 14, 'imdb': 66, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 
'year': 2014, 'poster': None, 'alternativeName': 'Sniper Pug', 'enName': None, 'movieLength': 4, 'names': [{'name': 'Снайпер Мопс'}, {'name': 'Sniper Pug'}], 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}}, {'id': 1165887, 'type': 'tv-series', 'externalId': {'kpHD': None, 'imdb': 'tt8595766'}, 'name': None, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'description': None, 'votes': {'kp': 14, 'imdb': 24195, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'year': 2018, 'poster': None, 'alternativeName': 'Yeh Meri Family', 'enName': None, 'movieLength': 30, 'names': [{'name': 'Yeh Meri Family'}], 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}, 'releaseYears': [{'start': 2018, 'end': 2018}]}, {'externalId': {'kpHD': None, 'imdb': 'tt0172007'}, 'rating': {'kp': 0, 
'imdb': 9, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'votes': {'kp': 13, 'imdb': 1171, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'id': 397288, 'type': 'tv-series', 'name': None, 'description': None, 'year': 1975, 'poster': {'url': 'https://st.kp.yandex.net/images/film_big/397288.jpg', 'previewUrl': 'https://st.kp.yandex.net/images/film_iphone/iphone360_397288.jpg'}, 'alternativeName': 'Grlom u jagode', 'enName': 
None, 'names': [{'name': 'Grlom u jagode'}], 'movieLength': 49, 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}, 'releaseYears': [{'start': 1975, 'end': 1975}]}, {'externalId': {'kpHD': None, 'imdb': 'tt0267277'}, 'rating': {'kp': 0, 'imdb': 9, 'filmCritics': 0, 
'russianFilmCritics': 0, 'await': 0}, 'votes': {'kp': 13, 'imdb': 1767, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': 0}, 'movieLength': 137, 
'id': 68255, 'type': 'movie', 'name': None, 'description': None, 'year': 1988, 'poster': None, 'alternativeName': 'Ashi Hi Banwa Banwi', 'enName': None, 'names': [{'name': 'Ashi Hi Banwa Banwi'}], 'shortDescription': None, 'logo': {'url': None}, 'watchability': {'items': None}}], 'total': 358, 'limit': 10, 'page': 3, 'pages': 36}

print((asd['docs'][9]))