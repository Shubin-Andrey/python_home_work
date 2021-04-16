counter = True
print('Введите строку, для завершения программы введите пустую строку')
with open('1_write.txt', 'a') as f:
    while counter:
        my_str = ''
        my_str = input('Введите строку')
        if my_str:
            f.write(f'{my_str}\n')
        else:
            counter = False
