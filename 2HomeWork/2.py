input_list_str=input('Введите значения через пробел')#
input_list=input_list_str.split()
print(input_list)
count=0
len_list=len(input_list)
if len_list%2 != 0:
    len_list-=1
while count<len_list:
    char=input_list[count]
    input_list[count]=input_list[count+1]
    input_list[count+1]=char;
    count+=2

print(input_list)