import requests
import json

#joke_str = response.text[15:]
#joke = json.loads(joke_str)['content']

def random_joke():
    url_joke = 'http://rzhunemogu.ru/RandJSON.aspx?CType=11'
    response = requests.get(url_joke)
    print(response.text)
    return response.text[12:-2]

test = random_joke()


#url = "https://v2.jokeapi.dev/joke/Any?type=single&lang=ru"

#response = requests.get(url)
#joke = response.json()

#print(joke)