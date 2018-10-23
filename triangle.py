from shape import Shape
#import matplotlib.pyplot as plt
#from numpy import *
import numpy as np

class Triangle(Shape):
    a = None #first side
    b = None #second side
    _k = None # angle between sides

    def __init__(self, a, b, k):
        super().__init__()
        self.a = a
        self.b = b
        self._k = round(np.pi / 180 * k, 2)


    @property
    def angle(self):
        return round(self._k * 180 / np.pi, 2)

    def area(self):
        return round((self.a * self.b * np.sin(self._k))/2, 2)

    def perimeter(self):
        return round(((self.a) ** 2 + (self.b) ** 2 - 2 * self.b * self.a * np.cos(self._k)) ** (1 / 2) + self.a + self.b, 2)

    def __str__(self):
        return "Triangle\n  sides: {0.a} x {0.b} angle: {0._k}".format(self)


    """""
    def picture(self):
        return plt.plot([0,self.a * cos(self._k)], [0, self.a * sin(self._k)]), plt.plot([0, self.b], [0,0]), plt.plot([self.a * cos(self._k), self.b], [self.a * sin(self._k), 0])
    """""