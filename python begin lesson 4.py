user_number = input('Введите целое положительное число')
max_number = int(user_number[0])
for i in range(len(user_number) - 1):
    if max_number <= int(user_number[i + 1]):
        max_number = int(user_number[i + 1])
print(max_number)
# второй вариант решения
user_number = input('Введите целое положительное число ')
length = len(user_number)
user_number = int(user_number)
max_number = user_number % 10
new_number = user_number // 10
for i in range(length - 1):
    if new_number % 10 > max_number:
        max_number = new_number % 10
        new_number = new_number // 10
    else:
        new_number = new_number // 10
print(max_number)
