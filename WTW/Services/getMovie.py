import requests
import json
import random

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
            return{'name': data['name'], 'image': data['poster'].get("url", "https://pbs.twimg.com/media/C5OTOt3UEAAExIk.jpg"), 'desc': data['description']}
        else:
            print(response.status_code)
            return(response.status_code)

    except requests.exceptions.HTTPError as error:
        print('Ошибочка'.format(error))
        return(response.status_code)

    except requests.exceptions.ConnectionError as error:
        print('Ошибка при получении фильма'.format(error))
        return(response.status_code)
        

def get_image(url):
    default_url = "https://pbs.twimg.com/media/C5OTOt3UEAAExIk.jpg"
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            photo = response.content
            return photo

    except requests.exceptions.HTTPError as error:
        print('Ошибочка'.format(error)) 
        response = requests.get(default_url)
        response.raise_for_status()
        if response.status_code == 200:
            photo = response.content
            return photo

    except requests.exceptions.ConnectionError as error:
        print('Ошибка при получении картинки'.format(error))
        response = requests.get(default_url)
        response.raise_for_status()
        if response.status_code == 200:
            photo = response.content
            return photo
    

def search_with_genre(genre):
    get_random_page = random.randint(1, 3)
    #get_random_score = round(random.uniform(7.4, 9.4), 1)

    url2 = f'https://api.kinopoisk.dev/v1/movie?page={get_random_page}&limit=10&name=%21null&description=%21null&logo.url=%21null&genres.name={genre}'
    response = requests.get(url=url2, headers=headers)
    response.raise_for_status()
    data = response.json()

    get_random_element = random.randint(0, (len(data['docs']) - 1))
    
    #rint(f'''страница {get_random_page}
    #элемент {get_random_element}
    #data - {data}''')

    output = {'name': data['docs'][get_random_element]['name'], 'desc': data['docs'][get_random_element]['description'], 'img_url': data['docs'][get_random_element]['poster'].get("url", "https://pbs.twimg.com/media/C5OTOt3UEAAExIk.jpg")}

    #print(output)
    return output

test = search_with_genre('детектив')