# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и
# сохраните в переменные, затем выведите на экран.

print('Hello Py!')
print("Hello Py!")
print(11 * 12)
print(10 // 3)
print(10 % 3)
print(2 ** 8)

x = 10
print(x)

x = 'hello'
print(x)

speed_car = 10

my_str = 'hello world!'
print(type(my_str))

my_int = 128
print(type(my_int))

my_float = 3.1415
print(type(my_float))

my_bool = True  # False
print(type(my_bool))

var = 'text'

var = 10
print(var)

print(10 > 1)
print(10 < 1)
print(3 != 3)

speed = 90
camera = True
print(speed > 79 and camera)

num = int(input('введите число: '))
print(num + 5)

orig_password = 'qwerty'
if input('Введите пароль: ') == orig_password:
    print('Успешная авторизация!')
else:
    print('пробуй ещё!')
print('end')

color = 'dsfs'
if color == 'red':
    print('красый')
elif color == 'green':
    print('зеленый')
elif color == 'black':
    print('черный')
print('.....')


num = 1
while num < 10:
    num += 1
    if num == 5:
        continue
    if num == 8:
        break
    print(num)

name = 'ivan'
surname = 'ivanov'
age = 50
print('Name:', name, "Surname:", surname, 'Age:', age)
print('Name: %s Surname: %s Age: %d' % (name, surname, age))
print('Name: {} Surname: {} Age: {}'.format(name, surname, age))
print(f'Name: {name:5} Surname: {surname} Age: {age}')
