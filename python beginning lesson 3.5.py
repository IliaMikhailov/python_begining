result = 0
while True:
    new_str = input('Введите строку из числе через пробел. Для завершения цикла в конце строки добавьте q')
    my_list = new_str.split()
    flag = False
    if new_str[-1] == 'q':
        my_list.pop()
        flag = True
    for i in range(len(my_list)):
        result += int(my_list[i])
    print(result)
    if flag == True:
        break
