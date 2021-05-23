with open('text_4.txt', 'r') as f:
    dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for line in f:
        file_str = line.split()
        file_str[0] = dict[file_str[0]]
        with open('text.txt', 'a') as f1:
            f1.write(' '.join(file_str))
            f1.write('\n')
