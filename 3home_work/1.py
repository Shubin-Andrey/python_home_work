def divide_1(int_first, int_second):
    try:
        result = int_first / int_second
        return result
    except ZeroDivisionError:
        print('на 0 делить нельзя')


print(divide_1(int(input('введите числитель')), int(input('введите знаменатель'))))
