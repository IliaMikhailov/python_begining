def func_2(name, surname, year, city, email, number):
    return (f'{name} {surname} {year} {city} {email} {number}')


user_name = input(' Введите ваше имя: ')
user_surname = input(' Введите вашу фамилию: ')
user_year = input(' Введите ваш год рождения: ')
user_city = input(' Введите ваш город: ')
user_email = input(' Введите ваш email: ')
user_phone = input(' Введите номер вашего телефона: ')
print(func_2(user_name, user_surname, user_year, user_city, user_email, user_phone))
