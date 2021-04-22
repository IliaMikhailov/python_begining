userNumber = input('Введите число ')
print(type(userNumber))
number_1 = int(userNumber)
number_2 = int(str(number_1) + str(number_1))
number_3 = int(str(number_1) + str(number_2))
sum = number_1 + number_2 + number_3
print(sum)
