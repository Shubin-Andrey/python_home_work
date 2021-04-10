def my_func(int_1, int_2, int_3):
    a = min(int_1, int_2, int_3)
    return (int_1 + int_2 + int_3 - a)


print(my_func(int(input('Введите первое число')),
              int(input('Введите второе число')),
              int(input('Введите третье число'))))
