import itertools
from sys import argv

def func_count(first_number):
    for i in itertools.count(first_number):
        print(i)
        if i >= 10:
            print('конец цикла')
            break


def func_cycle(new_list):
    count = 0
    for i in itertools.cycle(new_list):
        count += 1
        print(i)
        if count >= 10:
            print('конец цикла')
            break

func_count(int(argv[1]))
func_cycle(argv[1:])
