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
    
#Надо сделать рандомное подставление рейтинга от 7 до 10 и вставить в запрос + рандомная страница 1-5 + рандомный элемент списка
def search_with_genre(genre):
    get_random_page = random.randint(1, 2)
    get_random_score = round(random.uniform(7.4, 9.4), 1)
    get_random_element = random.randint(1, 9) - 1
    print(f'''страница {get_random_page}
    оценка {get_random_score}
        элемент списка {get_random_element}
    ''')
    url2 = f'https://api.kinopoisk.dev/v1/movie?page={get_random_page}&limit=10&name=%21null&description=%21null&rating.imdb={get_random_score}&logo.url=%21null&genres.name={genre}'
    response = requests.get(url=url2, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    '''
    print(data)
    print(len(data['docs']))
    print(data['docs'][get_random_element])
    '''
    output = {}
    if data['docs'][get_random_element]['poster']['url'] != None:
        if data['docs'][get_random_element]['description'] != None:
            output = {'name': data['docs'][get_random_element]['name'], 'desc': data['docs'][get_random_element]['description'], 'img_url': data['docs'][get_random_element]['poster']['url'] }
        else:
            output = {'name': data['docs'][get_random_element]['name'], 'img_url': data['docs'][get_random_element]['poster']['url'] }
    else:
        if data['docs'][get_random_element]['description'] != None:
            output = {'name': data['docs'][get_random_element]['name'], 'desc': data['docs'][get_random_element]['description']}
        else:
            output = {'name': data['docs'][get_random_element]['name']}

    #print(data['docs'][get_random_element]['name'])
    #print(data['docs'][get_random_element]['description'])


    #Добавить обработку получения описания и картинки, потому что будет дроп, если там ничего нет
    print(output)
    return output

test = search_with_genre('комедия')