userNumber = int(input('Введите время в секундах: '))
seconds = userNumber % 60
minutes = userNumber // 60
hours = 0
if minutes > 60:
    hours = userNumber // 3600
    minutes = minutes - hours * 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
