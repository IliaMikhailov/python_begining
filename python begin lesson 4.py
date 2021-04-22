userNumber = input('Введите целое положительное число')
maxNumber = int(userNumber[0])
for i in range(len(userNumber) - 1):
    if maxNumber <= int(userNumber[i + 1]):
        maxNumber = int(userNumber[i + 1])
print(maxNumber)
# второй вариант решения
userNumber = input('Введите целое положительное число ')
length = len(userNumber)
userNumber = int(userNumber)
maxNumber = userNumber % 10
newNumber = userNumber // 10
for i in range(length - 1):
    if newNumber % 10 > maxNumber:
        maxNumber = newNumber % 10
        newNumber = newNumber // 10
    else:
        newNumber = newNumber // 10
print(maxNumber)
