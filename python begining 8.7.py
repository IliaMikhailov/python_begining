class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'({self.a} + {self.b}i)'
    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}i'

if __name__ == '__main__':
    number_1 = ComplexNumber(2, 2)
    number_2 = ComplexNumber(4, 3)
    print(number_1)
    print(number_1,'+', number_2,'=', number_1 + number_2)
    print(f'{number_1} * {number_2} = {number_1 * number_2}')