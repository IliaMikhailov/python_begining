class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

if __name__ == "__main__":
    first_worker = Position("Иван", "Иванов", "рабочий", 12000, 8000)
    print(f'{first_worker.get_full_name()} зарабатывает {first_worker.get_total_income()} руб.')
    print(first_worker.name)
    print(first_worker.surname)
    print(first_worker.position)
    second_worker = Position("Петр", "Петров", "грузчик", 15000, 3000)
    print(second_worker.name)
    print(second_worker.get_full_name())
    print(second_worker.get_total_income())