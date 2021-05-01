def my_func(a, d, f):
    list = [a, d, f]
    list.sort()
    return list[-1] + list[1]


user_number_1 = int(input(' Введите первое число '))
user_number_2 = int(input(' Введите второе число '))
user_number_3 = int(input(' Введите третье число '))
print(my_func(user_number_1, user_number_2, user_number_3))
