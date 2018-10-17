# coding: utf8
from shape import Shape


class Rectangle(Shape):
    """
    Rectangular shape.
    """

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__() # wywołanie metody z klasy nadrzędnej
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    """
    Square shape as a specific rectangle.
    """

    def __init__(self, a):
        super().__init__(a, a)

        #repr - czytelnejszy obiekt dla programisty
        #str - ładnie dla urzytkownika
