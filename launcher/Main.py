'''
Created on Dec 28, 2017
Geometry
Main
@author: LeMatty
'''

from datamodel.Circle import Circle
from datamodel.Square import Square
from datamodel.Triangle import Triangle

if __name__ == '__main__':
    c1 = Circle(5)
    s1 = Square(5)
    t1 = Triangle(2, 3, 5, 4)

    print("Circle Area: " + str(c1.getArea()))
    print("Circle Perimeter: " + str(c1.getPerimeter()))
    print("Square Area: " + str(s1.getArea()))
    print("Square Perimeter: " + str(s1.getPerimeter()))
    print("Triangle Area: " + str(t1.getArea()))
    print("Triangle Perimeter: " + str(t1.getPerimeter()))
