# coding: utf8
from shape import Shape
#import matplotlib.pyplot as plt
#from numpy import *



class Rectangle(Shape):

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__() # wywołanie metody z klasy nadrzędnej
        self.a = a
        self.b = b

    def area(self):
        return round(self.a * self.b, 2)

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Rectangle \n  sides: {0.a} x {0.b}".format(self)


    """""
    def picture(self):
        return plt.plot([0, self.b], [0, 0]), plt.plot([0, self.b], [self.a, self.a]), plt.plot([0, 0], [0, self.a]), plt.plot([self.b, self.b], [0, self.a])
    """""

class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return "Square \n  side: {0.a}".format(self)


    """""
    def picture(self):
        return plt.plot([0, self.a], [0, 0]), plt.plot([0, self.a], [self.a, self.a]), plt.plot([0, 0], [0, self.a]), plt.plot([self.a, self.a], [0, self.a])
    """""