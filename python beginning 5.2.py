with open('file.txt', 'r') as f:
    number_str = 0
    for line in f:
        if line != '\n':
            number_str += 1
            print('Количество слов в строке = ', len(line.split()))
print('Количество строк в файле', number_str)
