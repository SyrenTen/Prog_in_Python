# Лабораторна робота №6

import matplotlib.pyplot as plt
import numpy as np

# Завдання 1
x = [1, 2, 3, 4, 5]


def calculate_y(x):
    return [val + 2 for val in x]


y = calculate_y(x)

plt.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='y = x + 2')
plt.title('Графік функції', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()


# Завдання 2
x = np.linspace(-6, 6, 100)

y1 = np.abs(x)
y2 = x ** 3
y3 = 0.5 * x

plt.plot(x, y1, label='$y = |x|$', color='blue', linestyle='--')
plt.plot(x, y2, label='$y = x^3$', color='red', linestyle='-')
plt.plot(x, y3, label='$y = 1/2x$', color='green', linestyle='-.')

plt.title('Графіки математичних функцій', fontsize=16, fontweight='bold', color='blue')
plt.xlabel('x', fontsize=14, color='red')
plt.ylabel('y', fontsize=14, color='red')
plt.legend(loc='lower right', fontsize=12)

plt.savefig('functions_grafs.png', dpi=300, bbox_inches='tight')
plt.savefig('functions_grafs.pdf', bbox_inches='tight')
plt.show()


# Завдання 3
def func1(x):
    return 5 * np.sin(1 / x) * np.cos(x ** 2 + 1 / x) ** 2


def func2(x):
    return 5 * np.sin(1 / x) * np.cos(x ** 2) ** 3


x1 = np.linspace(1, 4, 100)
x2 = np.linspace(-4, 4, 100)
y1 = func1(x1)
y2 = func2(x2)

# на одному полі
plt.figure(figsize=(10, 5))

plt.plot(x1, y1, label='y(x) = 5*sin(1/x)*cos(x^2+1/x)^2', color='blue', linestyle='-')
plt.plot(x2, y2, label='y(x) = 5*sin(1/x)*cos(x^2)^3', color='red', linestyle='--')

plt.title('Графіки функцій', fontsize=16, fontweight='bold')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))  # на різних полях фігури

plt.subplot(2, 1, 1)
plt.plot(x1, y1, label='y(x) = 5*sin(1/x)*cos(x^2+1/x)^2', color='blue', linestyle='-')
plt.title('Графік y(x) = 5*sin(1/x)*cos(x^2+1/x)^2', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x2, y2, label='y(x) = 5*sin(1/x)*cos(x^2)^3', color='red', linestyle='--')
plt.title('Графік y(x) = 5*sin(1/x)*cos(x^2)^3', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.show()


# Завдання 4
def count_vowels(text):
    vow = 'аеєиіїоуюя'
    vowel_count = {vowel: 0 for vowel in vow}
    for c in text:
        if c in vow:
            vowel_count[c.lower()] += 1
    return vowel_count


with open('l6_task4.txt', 'r', encoding='utf-8') as file:
    text = file.read()

vow_count = count_vowels(text)

# гістограма
vowels = list(vow_count.keys())
counts = list(vow_count.values())

x = np.arange(len(vowels))
plt.bar(x, counts, color='skyblue', edgecolor='black')

plt.title('Кількість голосних літер у тексті', fontsize=16)
plt.xlabel('Голосні літери', fontsize=14)
plt.ylabel('частота', fontsize=14)
plt.xticks(x, vowels)
plt.grid(True)

plt.savefig('vowels_histogram.png', dpi=300, bbox_inches='tight')
plt.show()


# Завдання 5
companies = ['Полісся', 'Грант', 'Міріса', 'AT trading', 'Trade F']
revenu = [10, 45, 19, 11, 15]

color = ['blue', 'green', 'yellow', 'red', 'purple']

explode = (0, 0.2, 0, 0, 0)  # грант відокремлений

# кругова діаграма
plt.figure(figsize=(8, 8))
plt.pie(revenu, labels=companies, autopct='%1.1f%%', colors=color, startangle=140, explode=explode)

plt.title('Валовий дохід підприємств')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.savefig('revenues_circle.png', bbox_inches='tight')
plt.show()


# Завдання 6
categ = ['MS Excel', 'MS Word', 'MS PowerPoint']
quart = ['I кв.', '|| кв.', '||| кв.', 'IV кв.']
sales = np.array([
    [112, 231, 178, 129],
    [187, 195, 118, 149],
    [167, 129, 70, 90]
])

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.figure(figsize=(10, 6))
bar_width = 0.2
for i in range(len(categ)):
    plt.barh(np.arange(len(quart)) + i * bar_width, sales[i], bar_width, color=colors[i], label=categ[i])

plt.title('Об`єми продажу книг в розрізі кварталів', fontsize=16)
plt.xlabel('Обсяг продажу', fontsize=14)
plt.ylabel('Квартал', fontsize=14)

plt.yticks(np.arange(len(quart)) + bar_width, quart)  # мітки
plt.legend()
plt.savefig('task6_sales.png', bbox_inches='tight')
plt.show()
