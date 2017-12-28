'''
Geometry
Circle Class
@author: LeMatty
'''
from math import pi


class Circle():

    def __init__(self, radius):
        self.r = radius

    # Calculate area
    def getArea(self):
        return pi * self.r ** 2

    # Calculate Perimeter
    def getPerimeter(self):
        return 2 * pi * self.r

    def __repr__(self):
        return "radius = '{}'".format(self.r)

    def __str__(self):
        return "radius = '{}'".format(self.r)
