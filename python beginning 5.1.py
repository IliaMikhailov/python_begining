with open('file.txt', 'w') as f:
    while True:
        user_str = input('Введите строку для файла. Нажмите Enter без ввода для завершения')
        if user_str == '':
            break
        else:
            f.write(user_str + '\n')
