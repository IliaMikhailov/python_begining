class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


new_list = []
while True:
    new_str = input('Введите строку из числе через пробел. Для завершения цикла в конце строки добавьте q ')
    klist = new_str.split()
    flag = False
    if new_str[-1] == 'q':
        klist.pop()
        flag = True
    for i in range(len(klist)):
        try:
            if klist[i].isdigit():
                klist[i] = int(klist[i])
                new_list.append(klist[i])
        except MyException:
            print('В введенной строке обнаружены символы')
    print(new_list)
    if flag == True:
        break
