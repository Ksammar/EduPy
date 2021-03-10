# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def personal_data(name, surname, birth_year, city, email, phone):
    print(f'{name} {surname} {birth_year} {city} {email} {phone}')


input_parameters = ['name', 'surname', 'year of birth', 'city of residence', 'email', 'phone']
personal_info = {}
for i in range(len(input_parameters)):
    personal_info.update({input_parameters[i]: input(f'insert {input_parameters[i]} ')})
personal_data(name=personal_info.get('name'),
              surname=personal_info.get('surname'),
              birth_year=personal_info.get('year of birth'),
              city=personal_info.get('city of residence'),
              email=personal_info.get('email'),
              phone=personal_info.get('phone'))
