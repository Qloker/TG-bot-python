import json


file_name = 'user_name.json'
file_path = 'd:/Рабочий стол/пн/TestGit/Shared/study/files and json/'
file = file_path + file_name

def get_stored_user_name():
    global file

    try:
        with open(file) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name

def greet_user():

    global file

    user_name = get_stored_user_name()
    print(user_name)

    if user_name:
        print('Hi' + ' ' + user_name)
    else:
        user_name = input('type username\n')
        with open(file, 'w') as f_obj:
            json.dump(user_name, f_obj)
    print('saved' + ' ' + user_name)
greet_user()