# exercise 1
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def length(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)


a = Point(5, 2)
b = Point(7, 9)
print(' ', a.__str__(), '\n', b.__str__(), '\n', a.length(b))


# exercise 2
def stair():
    n = int(input())
    for n in range(1, 46):
        n -= 1, 2
        print(n)


# exercise 3
def roman_to_integer():
    s = input('roman number to your liking:')
    i = 'I' == 1
    v = 'V' == 5
    x = 'X' == 10
    l = 'L' == 50
    c = 'C' == 100
    d = 'D' == 500
    m = 'M' == 1000


# exercise 4
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_2 = self.x + other.x
        y_2 = self.y + other.y
        return Vector(x_2, y_2)

    def __mul__(self, a):
        xtn = self.x * int(a)
        ytn = self.y * int(a)
        return Vector(xtn, ytn)

    def __rmul__(self, a):
        xtn = int(a) * self.x
        ytn = int(a) * self.y
        return Vector(xtn, ytn)


p_a = Vector(2, 7)
p_b = Vector(3, 5)
print((p_a + p_b), (p_a * 2), (3 * p_b))
