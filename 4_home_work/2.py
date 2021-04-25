my_list = [3, 5, 65, 3, 7, 678, 34, 43, 5, 7]
new_list = [el for i, el in enumerate(my_list) if i != 0 and el > my_list[i - 1]]
print(f'Новый список - {new_list}')
