class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            return f'Количество ячеек в первой клетке меньше чем во второй'

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, numbers_in_line):
        new_line = ''
        for j in range(1, self.number + 1):
            new_line += '*'
            if j % numbers_in_line == 0:
                new_line += '\n'
        return new_line


if __name__ == '__main__':
    first = Cell(1800)
    second = Cell(100)
    trird = first + second
    four = first - second
    five = first * second
    six = first / second
    print(first)
    print(second)
    print(trird)
    print(four)
    print(five)
    print(six)
    print(six.make_order(5))
