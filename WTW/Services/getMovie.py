import requests
import json

url = 'https://api.kinopoisk.dev/v1/movie/random'
API_KEY = 'HKZ4SGG-YPCMWDK-NDCEZ9M-T4FR0MR'
headers = {'accept': 'application/json', 'X-API-KEY': API_KEY}

def random_movie_search():
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            #print(data['name'])
            #print(data)
            #print(data['poster']['url'])
            #print(data['description'])
            return{'name': data['name'], 'image': data['poster']['url'], 'desk': data['description']}
        else:
            print(response.status_code)
            return(response.status_code)

    except requests.exceptions.HTTPError as error:
        print('Ошибочка'.format(error))
        return(response.status_code)

    except requests.exceptions.ConnectionError as error:
        print('Ошибка при соединении'.format(error))
        return(response.status_code)
        
#film = random_movie_search()
#print(film['desk'])

def get_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            photo = response.content
            return photo
        else:
            return 'Без фото'

    except requests.exceptions.HTTPError as error:
        print('Ошибочка'.format(error)) 
        return 'Без фото'

    except requests.exceptions.ConnectionError as error:
        print('Ошибка при соединении'.format(error))
        return 'Без фото'