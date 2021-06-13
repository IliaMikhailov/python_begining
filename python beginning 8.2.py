class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    user_number = input('Введите число для деления ')
    try:
        user_number = int(user_number)
        if user_number == 0:
            raise MyException('Деление на ноль ')
        print(200 / user_number)
    except MyException as err:
        print(err)
        exit(1)

