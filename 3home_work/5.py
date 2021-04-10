result = 0


def my_sum(args):
    global result
    for i in args:
        try:
            i = float(i)
            result = result + i
        except ValueError:
            print('В последовательности присутствует строка, она исключена из рассчетов')
    return result


my_list = []
counter = True
while counter:
    my_string = input('Введите числовые значения через пробел или "Q" для выхода')
    my_list = my_string.split()
    if my_string.upper() == "Q":
        counter = False
    else:
        result = my_sum(my_list)
    print(result)
