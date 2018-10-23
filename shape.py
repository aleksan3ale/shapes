# coding: utf8


class Shape(object):
    """
    Base class for all shapes.
    """


    def area(self):
        """
        Abstract method returning area of a shape.
        """

    def perimeter(self):
        """
        Abstract method returning shape perimeter.
        """
    #def title(self):
        """
        Set title
        """

    def summary(self):
        """
        Return summary of a shape.
        """
        return {
            'area': repr(self.area()),
            'perimeter': repr(self.perimeter())
        }
        """""
        'area': round(self.area(), 2),
        'perimeter': round(self.perimeter(), 2)
        """""

