import storage


class NumberTechnicCorrect(Exception):
    def __init__(self, txt):
        self.txt = txt


class Technic():
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Printer(Technic):
    def __init__(self, name, colour, number):
        self.colour = colour
        super().__init__(name, number)

    def __str__(self):
        return f'бренд: {self.name} цвет печати: {self.colour} количество:{self.number}'

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        if colour == 'black' or colour == 'colour':
            self.__colour = colour
        else:
            self.__colour = 'black'


class Monitor(Technic):
    def __init__(self, name, size, number):
        self.size = size
        super().__init__(name, number)

    def __str__(self):
        return f'бренд: {self.name} разрешение: {self.size} количество:{self.number}'


if __name__ == '__main__':
    while True:
        try:
            number = int(input('введите число'))
            if number < 1:
                raise NumberTechnicCorrect('количество не может быть меньше 1')
            else:
                break
        except NumberTechnicCorrect as err:
            print(err)
        except ValueError:
            print('Введена срока')

    m1 = Printer('hp', 'неправильный ввод цвета', 1)
    m2 = Printer('epson', 'colour', 2)
    m3 = Monitor('lg', '1960x1200', 1)
    new_storage = storage.Storage([[0, 0], [0, 0]])
    new_storage.new_item_in_storage(0, 0, m1)
    new_storage.new_item_in_storage(1, 1, m2)
    new_storage.new_item_in_storage(1, 0, m3)
    print(new_storage)
