my_list = []#
dict_list = []
new_dict = {}
count_line = int(input('Сколько вводить позиций'))

for counter in range(count_line):
    name_add = input('Введите наименование')
    price_add = int(input('Введите цену'))
    amount_add = int(input('Введите колличество'))
    count = input('Введите единицы измерения')
    my_dict = {'название': name_add, 'цена': price_add, 'количество': amount_add, 'eд': count}
    new_list = [counter + 1, my_dict]
    my_tuple = tuple(new_list)
    my_list.append(my_tuple)
    print(my_list)

for counter in my_dict.keys():
    for count_list in my_list:
        dict_list.append(count_list[1].get(counter))

    new_dict.update({counter: dict_list})
    dict_list = []

for counter in new_dict.keys():
    print(f'{counter} : {new_dict.get(counter)}')