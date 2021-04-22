start = int(input('Введите количество километров, которые пробегает спортсмен '))
maxDistance = int(input('Введите к какому результату должен стремиться спортсмен '))
count = 0
while maxDistance > start:
    start *= 1.1
    count += 1
print(f'За {count} дней спортсмен достигнет нужного результата')
