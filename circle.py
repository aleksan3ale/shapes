from shape import Shape
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

class Circle(Shape):
    r = None #radius

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return round(self.r ** 2 * np.pi, 2)

    def parameter(self):
        return 2 * np.pi * self.r

    def __str__(self):
        return "Circle \n  radius: {0.r}".format(self)

    def picture(self):
        i = arange(0, 2 * pi, .01)
        return plt.plot(self.r * sin(i), self.r * cos(i))
