start = int(input('Введите количество километров, которые пробегает спортсмен '))
max_distance = int(input('Введите к какому результату должен стремиться спортсмен '))
count = 1
while max_distance > start:
    start *= 1.1
    count += 1
print(f'За {count} дней спортсмен достигнет нужного результата')
