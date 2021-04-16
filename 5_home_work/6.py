with open('6_read.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    my_new_list = [el.split(':') for el in my_list]
    my_dict = {}
    new_sum = 0
    for i in range(len(my_new_list)):
        for el in my_new_list[i][1].split('-'):
            sum_str = ''
            for st in el:
                if st.isdigit():
                    sum_str = sum_str + st
            try:
                new_sum += int(sum_str)
            except:
                a = True
        my_dict[my_new_list[i][0]] = new_sum
        new_sum = 0
    print(my_dict)