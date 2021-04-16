import json
my_list = []
my_new_list = []
my_company_list = {}
with open('7_read.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    print(my_list)
    my_new_list = [el.split(' ') for el in my_list]

for el in my_new_list:
    k = int(el[3][:-1])
    my_company_list[el[0]] = int(el[2]) - k

k = 0
for el in my_company_list.keys():
    if my_company_list[el] > 0:
        k += my_company_list[el]

my_company_list['average_profit'] = k / len(my_company_list)
print(my_company_list)

with open("7_write.json", "w") as f:
    json.dump(my_company_list, f)

