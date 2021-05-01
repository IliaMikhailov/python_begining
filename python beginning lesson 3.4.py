def my_func(x, y):  # с помощью оператора **
    return x ** y


def my_func_2(x, y):  # с помощью цикла и умножения
    degree = 1
    for i in range(abs(y)):
        degree = degree * (1 / x)
    return degree


while True:
    user_number = input('Для выхода введите q. Введите x ')
    user_number_2 = input('Для выхода введите q. Введите y ')
    if user_number == 'q' or user_number_2 == 'q':
        break
    try:
        user_number = int(user_number)
        user_number_2 = int(user_number_2)
    except ValueError:
        print("Необходимо ввести натуральное число")
        continue
    if user_number_2 >= 0:
        print('Y должно быть меньше 0')
        continue
    if user_number <= 0:
        print('X должен быть больше 0')
        continue
    print(my_func(user_number, user_number_2))
    print(my_func_2(user_number, user_number_2))
    break
