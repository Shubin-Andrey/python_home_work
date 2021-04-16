with open('2_read.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    print(f'{my_list}- мои строки')
    print(f'{len(my_list)}- колличество строк')
    for i in range(len(my_list)):
        print(f'Строка номер {i+1} - Колличество слов в строке: {len(my_list[i].split())}')