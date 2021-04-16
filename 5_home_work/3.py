with open('3_read.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    print([el.split()[0] for el in my_list if el.split()[1].isdigit() and int(el.split()[1]) < 20000])
    print(f'Средний доход сотрудников: {sum([int(el.split()[1]) for el in my_list if el.split()[1].isdigit()])/len(my_list)}')