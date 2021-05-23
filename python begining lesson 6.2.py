class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__mass_1_metr = 25  # масса (кг) асфальта для необходимая для покрытия 1 м3
        self.__higth = 0.05  # высота асфальта в м

    def mass_road(self):
        return self._length * self._width * self.__mass_1_metr * self.__higth / 1000
    # м * м * кг / м3 * м = кг так как ответ нужно дать в тоннах делим на 1000


if __name__ == "__main__":
    first_road = Road(20, 5000)
    print(f'{first_road.mass_road():3} т')
