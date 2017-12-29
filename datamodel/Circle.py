'''
Geometry
Circle Class
@author: LeMatty
'''
from math import pi
from datamodel.Shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        self.r = radius
        super(Circle, self).__init__()

    # Calculate area
    def getArea(self):
        return pi * self.r ** 2

    # Calculate Perimeter
#     def getPerimeter(self):
#         return 2 * pi * self.r

    def __repr__(self):
        return "radius = '{}'".format(self.r)

    def __str__(self):
        return "radius = '{}'".format(self.r)
