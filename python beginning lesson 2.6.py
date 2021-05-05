goods = []
number_goods = int(input('Введите количество товаров для ввода'))
dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
dict_2 = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for a in range(0, number_goods):
    name = input('Введите название товара ')
    dict['название'].append(name)
    cost = input('Введите цену товара ')
    dict['цена'].append(cost)
    user_number = input('Введите количество товара ')
    dict['количество'].append(user_number)
    measure = input('Введите еденицу измерения')
    if measure not in dict['ед']:
        dict['ед'].append(measure)
    goods.append((a + 1, {'название': name, 'цена': cost, 'количество': user_number, 'ед': measure}))
print(goods)
# организация словаря из goods
for i in range(number_goods - 1):
    dict_2['название'].append(goods[i][1]['название'])
    dict_2['цена'].append(goods[i][1]['цена'])
    dict_2['количество'].append(goods[i][1]['количество'])
    if measure not in dict['ед']:
        dict_2['ед'].append(measure)
print(dict)
