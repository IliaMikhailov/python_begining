from abc import ABC, abstractmethod
class Closes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue(self):
        print('Производим расчёт расхода ткани на одежду')

class Coat(Closes):
    def __init__(self, size):
        self.size = size

    def tissue(self):
        super().tissue()
        return round(self.size / 6.5 + 0.5)


class Costume(Closes):
    def __init__(self, higth):
        self.higth = higth

    @property
    def higth(self):
        return self.__higth

    @higth.setter
    def higth(self, higth):
        if higth > 240 and higth < 30:
            self.__higth = higth
        else:
            self.__higth = 170

    def tissue(self):
        super().tissue()
        return round(self.__higth * 2 + 0.3)


if __name__ == '__main__':
    coat_1 = Coat(100)
    costume_1 = Costume(230)
    print(costume_1.tissue())
    print(coat_1.tissue() + costume_1.tissue())
    costume_2 = Costume(300)
    print(costume_2.tissue())
    costume_3 = Costume(10)
    print(costume_3.tissue())
