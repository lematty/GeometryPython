'''
Geometry
Triangle Class
@author: LeMatty
'''


class Triangle():

    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    # Calculate area
    def getArea(self):
        return (self.height * self.base) / 2

    # Calculate Perimeter
    def getPerimeter(self):
        return self.base + self.side1 + self.side2

    def __repr__(self):
        return "base = '{}', height = '{}', side1 = '{}', side2 = '{}'".format(self.base, self.height, self.side1, self.side2)

    def __str__(self):
        return "base = '{}'\nheight = '{}'\nside1 = '{}'\nside2 = '{}'".format(self.base, self.height, self.side1, self.side2)
