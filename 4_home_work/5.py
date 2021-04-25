from functools import reduce
def my_multiplication(first, second):
    return first * second
print(f'Мой список значений - {[el for el in range(100, 1000+1) if el % 2 == 0]}')
print(f'Их произведение - {reduce(my_multiplication, [el for el in range(100, 1000+1) if el % 2 == 0])}')
