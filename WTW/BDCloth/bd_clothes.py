import sqlite3
import json

conn = sqlite3.connect('clothing.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clothing (
    id INTEGER PRIMARY KEY,
    name TEXT,
    season TEXT,
    temp_min INTEGER,
    temp_max INTEGER,
    url TEXT
)
''')

data = [
    ("Куртка", "Зима", -30, 11, ["https://kosmo-shop.com/25192/kurtka-raduzhnaya-get-rainbow-mood-raduga-mnogocvetnaya-yarkaya-prikolnaya-veselaya.jpg", "https://framen.ru/d/kurtka-dlinnaja-s-klimat-kontrolem-761-autojack.jpg?h=800", "https://ae01.alicdn.com/kf/H7a65d3f8bf0c4404baf93aa59170366aE.jpg", "https://ae04.alicdn.com/kf/S2ba24b1e2df1447c9b7f5ad891b6834ee.jpg_640x640.jpg"]),
    ("Штаны", "Зима", -30, 11, ["https://kasta.ua/image/1035/s3/5/36/15/9735189/27884299/27884299_original.jpeg", "https://kasta.ua/image/1035/s3/5/36/15/9735189/27884299/27884299_original.jpeg"]),
    ("Аксессуар", "Зима", -30, 11, ["https://darvin-market.ru/upload/iblock/0f1/0f1afae5dd8a87086eb74a4fd5494546.jpeg"]),
    ("Футболка", "Зима", -30, 11, ["https://printbar.ru/upload/images/0b/0bb7483.jpg", "https://printbang.ru/img/products/85/muzhskaya-futbolka-pepe-fon-rikardo-milos-fleksonskiy-85979.jpg", "https://bukva-z.ru/upload/thumb/images/go/goh2c1zj0f4_590x0.jpg", "https://printbar.ru/upload/images/mp/mpvtuxi.jpg"])
]

for item in data:
    name, season, temp_min, temp_max, urls = item

    #Таким образом, в поле url будет сохранен список ссылок в формате JSON в виде строки. При чтении данных из БД необходимо будет десериализовать строку JSON обратно в список.
    url_str = json.dumps(urls)
    cursor.execute('INSERT INTO clothing (name, season, temp_min, temp_max, url) VALUES (?, ?, ?, ?, ?)', (name, season, temp_min, temp_max, url_str))

conn.commit()
conn.close()

