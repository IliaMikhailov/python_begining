first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [number for number in first_list if first_list.count(number) == 1]
print(new_list)