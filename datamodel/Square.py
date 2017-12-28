'''
Geometry
Square Class
@author: LeMatty
'''


class Square():

    def __init__(self, side):
        self.side = side

    # Calculate area
    def getArea(self):
        return self.side ** 2

    # Calculate Perimeter
    def getPerimeter(self):
        return 4 * self.side

    def __repr__(self):
        return "side = '{}'".format(self.side)

    def __str__(self):
        return "side = '{}'".format(self.side)
