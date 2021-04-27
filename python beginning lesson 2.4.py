user_str = input('Введите несколько слов через пробел')
new_list = user_str.split()
for i in enumerate(new_list):
    print(f'{i[0] + 1} - {i[1]:.10}')