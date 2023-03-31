import json


file_name = 'numbers.json'
file_path = 'd:/Рабочий стол/пн/TestGit/Shared/study/files and json/'
file = file_path + file_name

with open(file) as f_obj:
    numbers = json.load(f_obj)

print(numbers)