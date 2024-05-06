# Лабораторна робота №3

import math
import time
import datetime


# Завдання 1. Дано двозначне число. Перевірити істинність висловлювання "кожна цифра числа менша 6"
def statement(num):
    if num // 10 > 5 or num % 10 > 5:
        print('Висловлювання "кожна цифра числа менша 6" не є правдою')
    else:
        print('Висловлювання "кожна цифра числа менша 6" є правдою')


num = int(input('Введіть двозначне число: '))
if num < 10 or num > 99:
    print('Це число не є двозначним')
    exit()
else:
    statement(num)


# Завдання 2
num_list = [3, 100, 5, 24, 56, 8, 9]
new_list = list(map(lambda x: x * 2, num_list))
# new_list = list(map(lambda x: [x, x], num_list))
print(new_list)


# Завдання 3
string_list = 'Слово1, Слово2, Привіт, Слово4, Слово5, Слово6, Як, справи, Слово9, Слово10, Привіт11,' \
              'Слово12, Слово13, Слово14, Локі, Слово16, Слово17, Тор, Слово19, Слово20'
new_strl = ' '.join(map(lambda str: str.upper(), string_list.split()))
print(new_strl)


# Завдання 4
def count_positive_elem(arr):
    length = len(arr)
    if length % 2 != 0:
        middle = math.ceil(length / 2)
    else:
        middle = length // 2
    first_half = sum(1 for num in arr[:middle] if num > 0)
    second_half = sum(1 for num in arr[middle:] if num > 0)

    if first_half > second_half:
        return 'У першій половині послідовності додатних елементів більше'
    elif second_half > first_half:
        return 'У другій половині додатних елементів більше '
    else:
        return 'Додатних елементів однакова кількість в 1 і 2 половинах послідовності'


arr = []
mn = int(input('Введіть скільки елементів має бути в послідовності: '))
for _ in range(mn):
    arr.append(int(input()))
print(count_positive_elem(arr))


# Завдання 5
def sold_tickets():
    sold_a = int(input('Введіть кількість проданих квитків класу А: '))
    sold_b = int(input('Введіть кількість проданих квитків класу В: '))
    sold_c = int(input('Введіть кількість проданих квитків класу С: '))
    return sold_a, sold_b, sold_c


def count_sum(sold_a, sold_b, sold_c, a, b, c):
    print(f'Отриманий дохід від продажу квитків класу А: {sold_a * a}')
    print(f'Отриманий дохід від продажу квитків класу В: {sold_b * b}')
    print(f'Отриманий дохід від продажу квитків класу С: {sold_c * c}')
    print(f'Загальний дохід: {sold_a * a + sold_b * b + sold_c * c}')


cost_a = 100
cost_b = 78
cost_c = 35

sold_a, sold_b, sold_c = sold_tickets()
count_sum(sold_a, sold_b, sold_c, cost_a, cost_b, cost_c)


# Завдання 6
def recTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        bone = time.time() - start
        print(f'Функція відпрацювала за {bone} сек')
    return wrapper


@recTime
def read_cort(n):
    return tuple(range(n))


@recTime
def read_list(n):
    return list(range(n))


N = 100000
read_cort(N)
read_list(N)
