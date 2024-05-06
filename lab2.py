# Лабораторна робота №2

# Завдання 1
x = int(input('Введіть координату x: '))
y = int(input('Введіть координату y: '))

if x > 0 and y > 0:
    print('Точка знаходиться у I чверті')
elif x < 0 < y:
    print('Точка знаходиться у II чверті')
elif x < 0 and y < 0:
    print('Точка знаходиться у III чверті')
elif x > 0 > y:
    print('Точка знаходиться у IV чверті')
elif y == 0 and x != 0:
    print('Точка знаходиться на осі x')
elif x == 0 and y != 0:
    print('Точка знаходиться на осі y')
else:
    print('Точка знаходиться на початку координат')


# Завдання 2
x1 = float(input('Введіть х: '))
y1 = 0

if x1 < 0:
    y1 = x1
elif 0 <= x1 < 1:
    y1 = 0
elif x1 > 1:
    y1 = 2 * x1
print(y1)


# Завдання 3
a = int(input('Перше число: '))
b = int(input('Друге число: '))
type = input('Введіть операцію: ')
calc = 0
try:
    if type == '+':
        calc = a + b
    elif type == '-':
        calc = a - b
    elif type == '*':
        calc = a * b
    elif type == '/':
        try:
            calc = a / b
        # Завдання 4
        except ZeroDivisionError:
            calc = 'Ділення на нуль неможливе'
except ValueError:
    calc = 'Помилка введення'
print(calc)


# Завдання 5
info = 'Віталія, І-221д, Інтелектуальні та робототехнічні системи'
print(info[9:15])  # print(information.split()[1])
new_info = info.replace('Віталія', 'Маслова')
print(new_info)

calc_info = info.split()
print(len(calc_info))


# Завдання 6
list1 = ['1', '2', '3']
list2 = ['книжка', 'кіт', 'візерунок']
dict = {}

for i in range(len(list1)):
    dict[list1[i]] = list2[i]

print(dict)


# Завдання 7
# Відпрацюйте команди доповнення множини елементами, вилучення елементів, пошуку елемента

mnoj = set('абврстцй')
print(mnoj)
mnoj.add('ю')
print(mnoj)
mnoj.discard('а')
print(mnoj)
if 'ф' in mnoj:
    print('Такий елемент присутній')
else:
    print('Такого елементу немає')
