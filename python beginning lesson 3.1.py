def func(a, b):
    return a / b


first_number = int(input('Введите первое число '))
second_number = int(input('Введите второе число '))
try:
    print(f' Результат деления первого числа на второе: {func(first_number, second_number):.3}')
except ZeroDivisionError:
    print('Деление на ноль')
