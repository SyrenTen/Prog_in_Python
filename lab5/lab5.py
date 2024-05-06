# Лабораторна робота №5

import numpy as np
import csv

# Завдання 1
mass1 = np.array([1, 2, 3, 4, 5, 6])
mass2 = np.array([7, 8, 9, 10, 11, 12])

sum_mass = mass1 + mass2
print(f'Додавання: {sum_mass}')
minus_mass = mass1 - mass2
print(f'Віднімання: {minus_mass}')
multiple_mass = mass1 * mass2
print(f'Множення: {multiple_mass}')
division_mass = mass1 / mass2
print(f'Ділення: {division_mass}')

concat_mass = np.concatenate([mass1, mass2])
print(f'Метод конкатенації: {concat_mass}')

print(f'Максимальний елемент: {np.max(concat_mass)}')
print(f'Мінімальний елемент: {np.min(concat_mass)}')
print(f'Сума елементів: {np.sum(concat_mass)}')
print(f'Добуток елементів: {np.prod(concat_mass)}')


# Завдання 2
arr1 = np.array([5, 4, 1, 67, 32, 6, 16, 11, 9, 10, 9, 3, 13, 2, 15])

mean_value = np.mean(arr1)
mean_arr = arr1 - mean_value

print(mean_arr)

sorted_mean_arr = np.sort(mean_arr)
print(f'Відсортувати за зростанням:\n{sorted_mean_arr}')

with open('l5_task2.txt', 'w', encoding='utf-8') as file:
    file.write('Змінений масив:\n')
    file.write(str(mean_arr))
    file.write('\nВідсортований масив за зростанням:\n')
    file.write(str(sorted_mean_arr))


# Завдання 3
rand_mass = np.random.rand(20)
print(f'Одновимірний масив: {rand_mass}')

twod_rand_mass = rand_mass.reshape(4, 5)

twod_rand_mass += 10
print(f'Двовимірний масив збільшений на 10: {twod_rand_mass}')

with open('l5_task3.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Колонка 1', 'Колонка 2', 'Колонка 3', 'Колонка 4', 'Колонка 5'])
    for row in twod_rand_mass:
        writer.writerow(row)


# Завдання 4
array1 = np.random.randint(-15, 16, (3, 5))
print(array1)
for i in range(array1.shape[0]):
    for j in range(array1.shape[1]):
        if array1[i, j] < 0:
            array1[i, j] = -1
        else:
            array1[i, j] = 1
print(array1)


# Завдання 5
rand_array = np.random.rand(4, 6)
print(f'Двовимірний масив: {rand_array}')

# Сортування
sorted_array = np.sort(rand_array, axis=None)
print(f'\nВідсортований масив: {sorted_array}')

# мін значення масиву
min_value = np.min(rand_array)
print(f'\nМінімальне значення масиву: {min_value}')

sum_value = np.sum(rand_array)
print(f'Сума всіх елементів масиву: {sum_value}')

# Середнє знач масиву
mean_value = np.mean(rand_array)
print(f'Середнє значення масиву: {mean_value}')


# Завдання 6
cart_cords = np.random.rand(10, 3)
print(f'Декартові координати: {cart_cords}')

x, y, z = cart_cords[:, 0], cart_cords[:, 1], cart_cords[:, 2]
r = np.sqrt(x**2 + y**2 + z**2) # обчисл радіусу
theta = np.arccos(z / r)  # кут тета = arccos(z / r)
phi = np.arctan2(y, x)     # кут фі = arctan(y / x)

polar_cords = np.column_stack((r, theta, phi))
print(f'\nПолярні координати: {polar_cords}')
