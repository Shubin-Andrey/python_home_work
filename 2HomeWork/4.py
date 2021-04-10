input_list_str=input('Введите значения через пробел')#
input_list=input_list_str.split()
for counter in range(len(input_list)):
    in_ls=input_list[counter]
    print(counter+1,' - ', in_ls[:10])