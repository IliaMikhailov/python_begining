def int_func(word):
    return word.capitalize()


def int_func_2(str):
    new_str = str.split()
    for i in range(len(new_str)):
        new_str[i] = int_func(new_str[i])
    new_str = ' '.join(new_str)
    return new_str


user_str = input('Введите несколько слов через пробел ')
print(int_func_2(user_str))
