from sys import argv

script_name, working_time, time_price, prize = argv
try:
    result = (int(working_time) * int(time_price)) + int(prize)
    print(f'Результат рассчета зарплаты: {result}')
except ValueError:
    print('Введите не числовые данные')

