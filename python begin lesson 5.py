profit = int(input('Введите значение прибыли: '))
expense = int(input('Введите значение расходов: '))
if profit > expense:
    money = (profit - expense) / expense
    print(f'Фирма приносит прибыль. Рентабельность: {round(money, 3)}')
    numberWorkers = int(input('Введите количество работников: '))
    print(f'Прибыль на 1 сотрудника составляет: {round(profit / numberWorkers, 3)}')
else:
    print('Фирма работает в убыток')
