user_number = int(input('Введите время в секундах: '))
seconds = user_number % 60
minutes = user_number // 60
hours = 0
if minutes > 59:
    hours = user_number // 3600
    minutes = minutes - hours * 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
