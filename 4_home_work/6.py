from itertools import count, cycle
from sys import argv

script_name, script_mod_name, counter = argv
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11, 15]


def my_count(counter2):
    for el in count(int(counter2)):
        if el > 20:
            break
        else:
            print(el)


def my_cycle(counter2, my_list):
    с = 0
    for el in cycle(my_list):
        if с >= int(counter2):
            break
        else:
            print(el)
            с += 1


if script_mod_name == 'counter':
    my_count(counter)
elif script_mod_name == 'cycle':
    my_cycle(counter, my_list)
else:
    print(
        """        Вторым аргументом должно быть название модуля скрипта - "counter" или "cycle"
        а вторым счетчик повторений для "cycle"
        или началом отсчета для "counter" к примеру - "python 6.py counter 5" """
    )
