import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    new_result = []
    new_dict = {}
    new_dict_2 = {}
    count = 0
    summ = 0
    for line in f:
        new_str = line.split()
        new_dict[new_str[0]] = int(new_str[2]) - int(new_str[3])
    for keys in new_dict:
        if new_dict[keys] >= 0:
            summ += new_dict[keys]
            count += 1
    average = summ // count
    new_dict_2['average_profit'] = average
    new_result = [new_dict, new_dict_2]
    print(new_result)
with open('text.txt', 'w') as f1:
    json.dump(new_result, f1)
