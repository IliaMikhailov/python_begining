if __name__ == '__main__':
    print('PyCharm')
list = [1, 1, 1, 1, 1]
print(list)
list.append('строка')
print(list)
list[4] = 100
print(list)
list[-1] = ['2','3']
print(list)
list[-2] = (1, 5, 3)
print(list)
list.remove(1)
print(list)
print(list.count(1))
first = list[0]
last = list[-1]
a = 10
s = 15
a, s = s, a
print('s= ', s,'a=', a)
vocabulare = {1: 'value_1', 2: 'value_2', 3: 'value_3'}
vocabulare['str'] = 123
print(vocabulare)
vocabulare[('it','is')] = [11, 22, 33]
print(vocabulare)
print(vocabulare[1])
vocabulare.pop(2)
print(vocabulare)
print(vocabulare.keys())
