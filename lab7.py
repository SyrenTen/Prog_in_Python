# Лабораторна робота № 7

import numpy as np


# Завдання 1

# "2. видаліть координату z у класі Point3D і переконайтеся, що вона буде відсутня у всіх примірниках"
class Point3D:
    def __init__(self, x, y):  # def __init__(self, x, y, z):
        self.x = x
        self.y = y
        # self.z = z

    def __str__(self):
        # return f"Point3D({self.x}, {self.y}, {self.z})"
        return f"Point3D({self.x}, {self.y})"


point1 = Point3D(1, 2)  # point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5)  # point2 = Point3D(4, 5, 6)
point3 = Point3D(7, 8)  # point3 = Point3D(7, 8, 9)

print('Початкові координати:')
print(point1)
print(point2)
print(point3)

# Якщо у класі Point3D змінити self.x = x на, наприклад, self.x = x + 10,
# то коли будемо виводити координати екземплярів, замість заданих координат, отримаємо:
# Початкові координати:
# Point3D(11, 2, 3)
# Point3D(14, 5, 6)
# Point3D(17, 8, 9)

point1.x = 20
print(f'Зміна значення координати у екземплярі класу: {point1} \n')


# Завдання 2
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def set_mark(self, subject, mark):
        self.marks[subject] = mark

    def aver_marks(self):
        return sum(self.marks.values()) / len(self.marks)

    def print_mark(self):
        print('Оцінки студента:')
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')


student1 = Student('Маслова Віталія Максимівна')

student1.set_mark("Математика", 85)
student1.set_mark("Фізика", 90)
student1.set_mark("Хімія", 75)

print(f'ПІБ студента: {student1.name}')
student1.print_mark()
print(f'Середня оцінка: {student1.aver_marks()} \n')


# Завдання 3
class Triangle:
    def __init__(self, a, b, c):
        self.sides = np.array([a, b, c])

    def perimeter(self):
        return np.sum(self.sides)

    def square(self):
        p = self.perimeter() / 2
        return np.sqrt(p * np.prod(p - self.sides))


triangle1 = Triangle(12, 5, 8)

print("Периметр трикутника:", triangle1.perimeter())
print("Площа трикутника:", triangle1.square())
