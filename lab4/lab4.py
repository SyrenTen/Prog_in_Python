# Лабораторна робота №4

# Завдання 1
def calc_function(start, end, step):
    x = start
    result = []
    while x <= end:
        y = 2 * x - 1
        result.append((x, y))
        x += step
    return result


def result_to_file(filename, result):
    with open(filename, 'w') as file:
        for x, y in result:
            file.write(f'x = {x:.1f}, y = {y:.1f}\n')


s = -3
e = 3
st = 0.5

result = calc_function(s, e, st)
filen = 'function_result.txt'
result_to_file(filen, result)


# Завдання 2
filename = 'l4_task2.txt'
with open(filename, 'r') as file:
    text = file.read()

character = input('Введіть символ для підрахунку його кількості у файлі: ')

count = 0
ind = 0
while ind < len(text):
    if text[ind] == character:
        count += 1
    ind += 1

print(f'Символ "{character}" зустрічається у файлі {count} раз')


# Завдання 3
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p = arr[len(arr) // 2]
        a = [x for x in arr if x < p]
        b = [x for x in arr if x == p]
        c = [x for x in arr if x > p]
        return quick_sort(a) + b + quick_sort(c)


def find_element(mass, value):
    return value in mass


def find_five_min(mass):
    sort_arr = quick_sort(mass)
    return sort_arr[:5]


def calc_average(mass):
    return sum(mass) / len(mass) if mass else 0


def remove_duplic(mass):
    return list(set(mass))


def read_lists(filename):
    with open(filename, 'r') as file:
        lists = []
        for line in file:
            list_elements = list(map(int, line.split()))
            lists.append(list_elements)
    return lists


def write_results(filename, result):
    with open(filename, 'a', encoding='utf-8') as file:
        for r in result:
            file.write(str(r) + "\n")


filename = 'l4_task3.txt'
lists = read_lists(filename)
results = []

for arr in lists:
    sortedmass = quick_sort(arr)
    found = find_element(arr, 5)  # можна обрати інше число
    fiv_min = find_five_min(arr)
    average = calc_average(arr)
    no_repeat = remove_duplic(arr)

    results.append(f'Швидке сортування: {sortedmass}')
    results.append(f'Пошук елементу: {found}')
    results.append(f'Перші п`ять мін елементи: {fiv_min}')
    results.append(f'Середнє арифметичне: {average}')
    results.append(f'Без повторів: {no_repeat}')

write_results('task3_results.txt', results)


# Завдання 4
# З'ясувати, чи є в ньому рядок, який розпочинається з літери "Т".
# Якщо так, то визначити номер першого з таких рядків.
def find_line_starts_T(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        line_number = 1
        for line in file:
            if line.strip().startswith(('Т', 'T')):  # По завданню не зрозуміло це має бути англ чи укр "Т"
                return line_number
            line_number += 1
    return None  # якщо такого рядка немає


line_num = find_line_starts_T('l4_task4.txt')
if line_num is not None:
    print(f'Номер першого рядка, що починається з "Т": {line_num}')
else:
    print('У файлі немає рядка, що починається з "Т"')
