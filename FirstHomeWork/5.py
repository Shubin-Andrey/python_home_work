proceeds = input('Введите прибыль')
costs = input('Введите издержки')

if proceeds > costs:
    profit = int(proceeds) - int(costs)
    print(f'Фирма получила прибыль{profit} \n Рентабельность составила {profit / int(proceeds)}')
    count = input('Введите колличество сотрудников')
    print(f'Прибыль на каждого сотрудника: {profit/int(count)}')

elif proceeds < costs:
    damages = int(costs) - int(proceeds)
    print(f'Убыток составил {damages}')
    count = input('Введите колличество сотрудников')
    print(f'Убыток на каждого сотрудника: {damages/int(count)}')

else:
    print('Отработали в 0')

out=input('Нажмите на клавишу enter для выхода')