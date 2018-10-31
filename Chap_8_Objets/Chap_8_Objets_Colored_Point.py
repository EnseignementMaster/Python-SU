__author__ = 'lantos'

from Chap_8_Objets.Chap_8_Objets_Point import *


class Colored_Point(Point):
    "A point with a color"

    def __init__(self, x, y, color):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            Point.__init__(self, x, y)
        else:
            raise TypeError("wrong type for x, y")
        if isinstance(color, str):
            self.__color = color
        else:
            raise TypeError("wrong type for color")

    def __str__(self):
        return Point.__str__(self) + " in " + self.__color
        # return "(" + str(self.x) + ", " + str(self.y) + ") in "+self.color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


p = Colored_Point(0.0, 0.0, "red")
print(p)
p.translate(1.0, 2.0)
print(p)
p.translate(-2.0, -3.0)
print(p)
print(type(p))
p = Colored_Point(0.0, 0.0, "red")
print("p est un ", type(p), "Est-ce un Point? ", type(p) == Point)
print("p est un ", type(p), "Est-ce un Point? ", type(p) == Colored_Point)

print("p est un ", type(p), "Est-ce un Point? ", isinstance(p, Point))
print("p est un ", type(p), "Est-ce un Point? ", isinstance(p, Colored_Point))
