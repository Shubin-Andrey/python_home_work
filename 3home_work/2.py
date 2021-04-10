def user_1(first_name, second_name, birthday, city, email, phone):
    print(f'{first_name} {second_name}, {birthday}, {city}, {email}, {phone}')


user_dict = {'first_name': '', 'second_name': '', 'birthday': '', 'city': '', 'email': '', 'phone': ''}
for name in user_dict.keys():
    user_dict[name] = input(f'Введите {name}')
user_1(first_name=user_dict['first_name'], second_name=user_dict['second_name'],
       birthday=user_dict['birthday'], city=user_dict['city'],
       email=user_dict['email'], phone=user_dict['phone'])
