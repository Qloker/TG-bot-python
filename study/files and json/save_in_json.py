import json

file_name = 'numbers.json'
file_path = 'd:/Рабочий стол/пн/TestGit/Shared/study/files and json/'
file = file_path + file_name
numbers = [1, 123, 32131, 4]


with open(file, 'w') as file_object:       #as file_object: это переменная 
    json.dump(numbers, file_object)