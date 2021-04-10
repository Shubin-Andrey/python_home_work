def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    if y == 0:
        return 1
    return 1 / x * my_func_2(x, y + 1)


def my_func_3(x, y):
    result = 1
    for i in range(abs(y)):
        result = 1 / x * result
    return result


while True:
    x = input('Введите действительное положительное число')
    try:
        x = float(x)
        if x >= 0:
            break
        else:
            print('ПОЛОЖИТЕЛЬНОЕ!!! число')
    except ValueError:
        print('Я сказал число')
while True:
    y = input('Введите целое отрицательное число')
    try:
        y = int(y)
        if y < 0:
            break
        else:
            print('ОТРИЦАТЕЛЬНОЕ число!!!')
    except ValueError:
        print('Я сказал целое число')

print(my_func_1(x, y), 'Через **')
print(my_func_2(x, y), 'Через вызов функии самой себя')
print(my_func_3(x, y), 'Через цикл')
# Не могу понять почему значения различаются. Округление????
#"""Введите действительное положительное число2.6
#Введите целое отрицательное число-5
#0.00841653357321576 Через **
#0.008416533573215758 Через вызов функии самой себя
#0.008416533573215758 Через цикл"""
