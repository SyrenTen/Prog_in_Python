# Лабораторна робота № 8

import numpy as np


# Завдання 1
class Circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return np.pi * self.rad ** 2

    def circuit(self):
        return 2 * np.pi * self.rad


circle1 = Circle(5)
print(f'Площа круга: {circle1.area()}')
print(f'Довжина кола: {circle1.circuit()}')


# Завдання 2
class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed


car1 = Car('KIA', 'Sorento', 2019)

for _ in range(6):
    car1.accelerate()
    print(f'Швидкість: {car1.get_speed()}')

for _ in range(5):
    car1.brake()
    print(f'Швидкість: {car1.get_speed()}')


# Завдання 3
class MainClass:
    def __init__(self, text=""):
        self.text = text

    def set_text(self, text):
        self.text = text


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number


main = MainClass('Привіт')
print(f'Текст головного класу: {main.text}')

sub = SubClass('Світ', 42)
print(f'Текст класу-нащадка: {sub.text}')
print(f'Число класа-нащадка: {sub.number}')
