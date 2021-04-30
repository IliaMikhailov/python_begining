new_list = [7, 5, 3, 3, 2]
while True:
    user_number = input('Для выхода введите q. Введите новый элемент рейтинга: ')
    if user_number == 'q':
        break
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("Необходимо ввести натуральное число")
        continue
    for i in range(len(new_list)):
        if user_number >= new_list[i]:
            new_list.insert(i, user_number)
            break
         else:
            new_list.append(user_number)
            break
print(new_list)
