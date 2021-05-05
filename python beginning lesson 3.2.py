def func_2(**name):
    for key, value in name.items():
        print(f'{key} is {value}')


func_2(user_name = 'Иван', user_surname = 'Иванов', user_year = '2000', user_city = 'Санкт-Петербург', user_email = '@gmail.com', user_phone = '7777777')
