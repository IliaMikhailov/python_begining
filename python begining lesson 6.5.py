class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Нарисована {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Нарисован {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Нарисован {self.title}'

if __name__ == "__main__":
    f1 = Stationery("Блокнот")
    print(f1.draw())
    f2 = Pen("Ручка")
    print(f2.draw())
    f3 = Pencil("Карандаш")
    print(f3.draw())
    f4 = Handle("Маркер")
    print(f4.draw())
