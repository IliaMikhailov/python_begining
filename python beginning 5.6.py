def cut_str(str):  # функция убирает ненужные скобки после количества часов
    for i in range(len(str)):
        start_remove = str.find('(')
    return str[:start_remove]


def int_str(str):  # функция переводит в числовой формат данные
    if str == '-':
        return 0
    if str.isdigit():
        return int(str)


new_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:  # открываем для чтения файл с предметами и часами
    dict_lessons = {'Fizra': 'физкультура', 'Math': 'математика', 'History': 'История',
                    'Physics': 'Физика', 'Informatics': 'информатика', 'Literature': 'литература',
                    'Russian': 'русский язык'}  # словарь предметов
    for line in f:
        key_index = line.find(":")  # ищем индекс ":" для определения предмета
        new_str = line.split()
        new_str[0] = dict_lessons[line[:key_index]]  # меняем английское название на русское
        for i in range(1, len(new_str)):  # цикл для подготовки данных для занесения в словарь
            if new_str[i].find('(') != -1:
                new_str[i] = cut_str(new_str[i])
            new_str[i] = int_str(new_str[i])
        new_dict[new_str[0]] = sum(new_str[1:])  # заполняем словарь
    print(new_dict)
