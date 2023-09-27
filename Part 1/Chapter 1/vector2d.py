"""
vector2d.py: упрощенный класс, демонстрирующий некоторые специальные методы
"""
import math


class Vector:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector ({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x=x, y=y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Сложение векторов

v1 = Vector(3, 4)
v2 = Vector(2, 1)
v3 = v1 + v2
print(v3)
print(abs(v1))
print(v1 * 3)
print(bool(v3))
