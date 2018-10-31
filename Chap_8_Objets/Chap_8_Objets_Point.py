__author__ = 'lantos'
import types


class Point(object):  # Convention: an Object name is capitalized
    """
    a 2D Positive Point
    """

    def __init__(self, x, y):  # initialisation (remplace le constructeur)
        """
        initialize the point
        """
        if x < 0.0:
            self.__x = 0.0
        else:
            self.__x = x

        if y < 0.0:
            self.__y = 0.0
        else:
            self.__y = y

        self.__private = 1

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __nonzero__(self):
        return not (self.__x == 0.0 and self.__y == 0.0)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def translate(self, dx, dy):
        """
        Computes the area of the rectangle
        """
        self.x = self.__x + dx
        self.y = self.__y + dy

    @property
    def x(self):
        """I'm the 'x' property."""
        return self.__x

    @x.setter
    def x(self, x):
        """I'm the 'x' property."""
        # print("appel du setter de x")
        if x < 0.0:
            self.__x = 0.0
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if y < 0:
            self.__y = 0.0
        else:
            self.__y = y
