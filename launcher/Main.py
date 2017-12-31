'''
Created on Dec 28, 2017
Geometry
Main
@author: LeMatty
'''

from datamodel.Circle import Circle
from datamodel.Square import Square
from datamodel.Triangle import Triangle
from builtins import str

if __name__ == '__main__':
    # Circles
    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle(7)
    circleList = ["Circle", c1, c2, c3]

    # Squares
    s1 = Square(5)
    s2 = Square(6)
    s3 = Square(7)
    squareList = ["Square", s1, s2, s3]

    # Triangles
    t1 = Triangle(2, 3, 5, 4)
    t2 = Triangle(3, 4, 6, 5)
    t3 = Triangle(4, 5, 7, 6)
    triangleList = ["Triangle", t1, t2, t3]

    # All Shapes
    shapesList = [circleList, squareList, triangleList]

    # Output
    for i in shapesList:
        counter = 0
        for j in i:
            if type(j) is str:
                print("\n" + j)
                shape = j
            else:
                print(j)
                print("%s %d's Area :      %.02f" %
                      (shape, counter, j.getArea()))
                print("%s %d's Perimeter : %.02f\n" %
                      (shape, counter, j.getPerimeter()))
            counter += 1
