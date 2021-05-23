class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f'машина поехала'

    def stop(self):
        return f'машина остановилась'

    def turn_direction(self, direction):
        return f'машина поехала {direction}'

    def show_speed(self):
        return f'машина едет со скоростью {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости'
        else:
            return f'машина едет со скоростью {self.speed}'


class SportCar(Car):
    def go_turbo(self):
        return f'машина ускорилась до {self.speed + 20}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости'
        else:
            return f'машина едет со скоростью {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


if __name__ == "__main__":
    first_car = Car(50, 'синий', "Lada")
    print(f'{first_car.speed} {first_car.name} \n{first_car.go()}\n{first_car.turn_direction("направо")}')
    second_car = TownCar(70, 'красный', "Kia")
    print(f'{second_car.speed} {second_car.name} \n{second_car.go()}\n{second_car.turn_direction("налево")} \n{second_car.show_speed()}')
    third_car = PoliceCar(90, "белый", "Нива")
    print(third_car.is_police)
    print(second_car.is_police)
    four_car = SportCar(110, 'жёлтый', 'Lexus')
    print(four_car.go_turbo())
