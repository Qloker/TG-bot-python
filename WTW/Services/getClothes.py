import sqlite3
import random
import json
def get_clothing_by_temp(temp):
    conn = sqlite3.connect('clothing.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT name, url FROM clothing
    WHERE temp_min <= ? AND temp_max >= ?
    ''', (temp, temp))

    data = cursor.fetchall()
    result = []

    for i in range(len(data)):
        result.append((data[i][0], json.loads(data[i][1])))     

    conn.close
    return result

tests = get_clothing_by_temp(-1)

dic_cloth = {}
#print(tests)
for i in range(len(tests)):
    dic_cloth[tests[i][0]] = random.choice(tests[i][1])
#print(dic_cloth)