result = 0
while True:
    new_str = input('Введите строку из числе через пробел. Для завершения цикла в конце строки добавьте q')
    list = new_str.split()
    flag = False
    if new_str[-1] == 'q':
        list.pop()
        flag = True
    for i in range(len(list)):
        result += int(list[i])
    print(result)
    if flag == True:
        break
