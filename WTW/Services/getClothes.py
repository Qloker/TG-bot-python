import sqlite3

def get_clothing_by_temp(temp):
    conn = sqlite3.connect('clothing.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT name, url FROM clothing
    WHERE temp_min <= ? AND temp_max >= ?
    ''', (temp, temp))

    result = cursor.fetchall()

    conn.close
    return result

tests = get_clothing_by_temp(0)
print(tests)
print(tests[0])