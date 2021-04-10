my_list = [7, 5, 3, 3, 2]#

new_int = int(input('Введите целое число'))
my_list.append(new_int)
counter = True
a = len(my_list) - 1
while counter:
    if my_list[a-1] < my_list[a]:
        k = my_list[a-1]
        my_list[a-1] = my_list[a]
        my_list[a] = k
    else:
        counter = False
    if a != 1:
        a -= 1
print(my_list)