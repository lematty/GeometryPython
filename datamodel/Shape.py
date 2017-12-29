'''
Geometry
Shapes Abstract Class
@author: LeMatty
'''

import abc


class Shape(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getArea(self): pass

    @abc.abstractmethod
    def getPerimeter(self): pass
