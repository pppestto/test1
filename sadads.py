database = {'Joseph': {'age': 27, 'job': 'Тим лид', 'access': 'admin', 'password': '1234', 'blocked': False}}
#{name: {age: int, job: str, access: str, password: str, blocked: bool}}

def add_user():
    name = input('Введите ваше имя: ')
    age = input('Введите ваш возраст: ')
    job = input('Введите вашу работу: ')
    password = input('Введите ваш пароль: ')
    access = 'user'
    blocked = False
    database[name] = {'age': age, 'job': job, 'access': access, 'password': password}
    return ''

def change_user(name, access):
    changing_name = input('Чьи данные нужно изменить?')
    if name == changing_name:
        changing_data = input('Что вы хотите изменить?')
        if changing_data.lower() == 'возраст':
            try:
                database[changing_name]["age"] = int(input('Введите возраст'))
            except:
                print('Ответ должен быть числом')
        elif changing_data.lower() == 'работа':
            database[changing_name]["job"] = input('Введите место работы')
        elif changing_data.lower() == 'пароль':
            database[changing_name]["password"] = input('Введите новый пароль')
    else:
        if access == 'admin':
            question = input('Какие данные вы хотите изменить?')
            if question.lower == 'уровень доступa':
                database[changing_name]["access"] = input('Введите уровень пользователя')
            elif question.lower() == 'доступ':
                database[changing_name]["blocked"] = input('Хотите ли вы заблокировать пользователя? (True/False)')
            else:
                    print('У вас нет доступа')
        else:
            warning = input('В доступе отказано')
