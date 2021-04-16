dict_translate = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
new_list = []
with open('4_read.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    for el in my_list:
        new_char_dict = el.split()
        new_char_dict[0] = dict_translate[new_char_dict[0]]
        new_list.append(new_char_dict)
print(new_list)

with open('4_write.txt', 'w', encoding='utf-8') as f:
    new_char_dict = [' '.join(el) for el in new_list]
    print(new_char_dict)
    for el in new_char_dict:
        f.write(f'{el} \n')

