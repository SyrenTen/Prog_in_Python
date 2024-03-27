# Лабораторна робота №1

import math

# Завдання 1

print('І-221д, Маслова Віталія')
a1 = 1  # ціле число
a2 = -2.0  # дійсне число
print(a1, a2)
print(type(a1), type(a2))

# Завдання 2

b1 = int(input('Введіть b1: '))
b2 = int(input('Введіть b2: '))

info = 'Виконуємо додавання(+) b1 та b2: {op1}\n Виконуємо віднімання(-): {op2}\n Виконуємо множення(*): {op3}\n' \
       'Виконуємо ділення(/): {op4}\n Залишок від ділення(%): {op5}'
print(info.format(op1=b1 + b2, op2=b1 - b2, op3=b1 * b2, op4=b1 / b2, op5=b1 % b2))

# Завдання 3

n = int(input('Введіть кількість друзів: '))
m = int(input('Введіть суму рахунку: '))

# percent_m = m*15/100
new_m = m + m * 15 / 100

oplata = new_m / n
print(f'Кожен з друзів має оплатити по {oplata:.2f} грн.')

# Завдання 4, Варіант 10

x = int(input('Введіть х: '))

y = math.exp(2) * math.log10(x ** 4) * (((x - 0.5) ** 2 - math.cos(x)) / (math.sqrt(abs(x + 1) + abs(x))))

print(y)