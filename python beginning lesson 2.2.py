user_text = input('Введите несколько значений через пробел')
new_list = user_text.split()
for i in range(0, len(new_list) - 1, 2):
    new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
print(new_list)


