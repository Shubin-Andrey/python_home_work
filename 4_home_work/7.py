def fact(n):
    for el in range(int(n)):
        yield el


result = 1
n = input('От какого числа брать факториал?')
my_str = ''
for el in fact(n):
    counter = el + 1
    result *= counter
    my_str += str(counter) + ' * '

print(f'Факториал числа : {my_str[:-3]} = {result}')

