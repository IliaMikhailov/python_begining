with open('file.txt', 'r') as f:
    dict = {'фамилия': [], 'оклад': []}
    number_workers = 0
    for line in f:
        my_str = line.split()
        dict['фамилия'].append(my_str[0])
        dict['оклад'].append(int(my_str[1]))
        number_workers += 1
    for i in range(number_workers):
        if dict['оклад'][i] < 20000:
            print(dict['фамилия'][i])
    print(sum(dict['оклад']) // number_workers)
