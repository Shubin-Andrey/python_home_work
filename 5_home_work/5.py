from random import randint

with open('5_write.txt', 'w', encoding='utf-8') as f:
    i = 0
    while i != 10:
        f.write(f'{randint(0, 100)} ')
        i += 1

my_list = []
with open('5_write.txt', 'r', encoding='utf-8') as f:
    my_list = f.read().split()
    print(f'Сумма всех чисел из файла => {sum([int(el) for el in my_list])}')
