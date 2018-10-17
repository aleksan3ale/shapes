from shape import Shape
import numpy as np

class Parallelogram(Shape):
    a = None #one side of parallelogram
    b = None #height of the parallelogram
    _k = None # angle between sides

    def __init__(self, a, b, k):
        super().__init__()
        self.a = a
        self.b = b
        self._k = np.pi / 180 * k

    @property
    def angle(self):
        return round(self._k * 180 / np.pi, 2)

    def area(self):
        return round(self.a * self.b * np.sin(self._k), 2)

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return "Parallelogram has sides   {0.a} x {0.b}".format(self)


class Dimond(Parallelogram):

    def __init__(self, a, k):
        super().__init__(a, a, k)

    def __str__(self):
        return "Dimond has sides  a = {0.a}, b = {0.b}".format(self)
