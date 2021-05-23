import storage, printer


class NumberCount(Exception):
    def __init__(self, txt):
        self.txt = txt

class LenStorage(Exception):
        def __init__(self, txt):
            self.txt = txt


new_storage_x = []
new_storage_y = []
while True:
    try:
        user_str = input('Для начала созданим склад.\n Введите размеры склада: ')
        new_str = user_str.split()
        number_shelvings = int(new_str[0])
        number_floors = int(new_str[1])
        break
    except (ValueError, IndexError):
        print('Введите 2 числа через пробел')
        continue
for a in range(number_floors):
    new_storage_y.append(0)
for b in range(number_shelvings):
    new_storage_x.append(new_storage_y)
print(new_storage_x)
new_storage = storage.Storage(new_storage_x)
print('Необходимо заполнить новый склад оргтехникой \n')
while True:
    user_str = input('Для того, чтобы добавить на склад принтер введите 1\n'
                     'Для того, чтобы убрать, то что лежит в ячейке нажмите 2\n'
                     'Для того, чтобы добавить на склад монитор введите 3\n'
                     'Для вывода текущей заполненности склада введите 4 \n'
                     'Для выхода введите q')
    if user_str == '1':
        user = input('Введите данные принтера.\n'
                     'Формат для ввода: "бренд" "цвет печати:(black или colour)" "количество" ')
        user_item = user.split()
        try:
            user_item[2] = int(user_item[2])
            if user_item[2] < 0:
                raise NumberCount('Должно быть больше 0')
        except NumberCount as err:
            print(err)
            continue
        except ValueError:
            print('Количество должно быть числом')
        new_storage.new_item_in_storage(printer.Printer(user_item[0], user_item[1], user_item[2]))
    elif user_str == '2':
        user = input('Введите ячейку, чтобы убрать содержимое.\n'
                     'Формат для ввода: "№ стеллажа" "№ полки"')
        user_item = user.split()
        try:
            user_item[0] = int(user_item[0])
            user_item[1] = int(user_item[1])
            if user_item[0] < 0 or user_item[0] > number_shelvings:
                raise LenStorage(f'Нумерация ячеек от 0 до {len(new_storage)}')
        except LenStorage as err:
            print(err)
        new_storage.del_from_storage(user_item[0], user_item[1])
    elif user_str == '3':
        user = input('Введите данные монитора.\n'
                     'Формат для ввода: "бренд" "разрешение" "количество" ')
        user_item = user.split()
        user_item[2] = int(user_item[2])
        new_storage.new_item_in_storage(printer.Monitor(user_item[0], user_item[1], user_item[2]))
    elif user_str == '4':
        print(new_storage)
    elif user_str == 'q':
        break
    else:
        print('Неверный ввод')
        continue
