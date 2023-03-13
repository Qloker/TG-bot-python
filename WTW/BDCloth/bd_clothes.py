import sqlite3

conn = sqlite3.connect('clothing.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clothing (
    id INTEGER PRIMARY KEY,
    name TEXT,
    season TEXT,
    temp_min INTEGER,
    temp_max INTEGER,
    url, TEXT
)
''')

cursor.execute('''
INSERT INTO clothing (name, season, temp_min, temp_max, url)
VALUES 
    ("Куртка", "Зима", -30, 0, "https://kosmo-shop.com/25192/kurtka-raduzhnaya-get-rainbow-mood-raduga-mnogocvetnaya-yarkaya-prikolnaya-veselaya.jpg"),
    ("Штаны", "Зима", -30, 0, "https://kasta.ua/image/1035/s3/5/36/15/9735189/27884299/27884299_original.jpeg"),
    ("Аксессуар", "Зима", -30, 0, "https://darvin-market.ru/upload/iblock/0f1/0f1afae5dd8a87086eb74a4fd5494546.jpeg")
''')

conn.commit()

conn.close()