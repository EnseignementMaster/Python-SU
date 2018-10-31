class Rectangle():
    """
    Object to modelize a rectangle
    """

    def __init__(self, x1, y1, x2, y2):
        """
        initialize the rectangle
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

    def __str__(self):
        return "Je suis un rectangle"

    def computeArea(self):
        """
        Computes the area of the rectangle
        """
        self.area = abs(self.x1 - self.x2) * abs(self.y1 - self.y2)
        return self.area

    @property
    def x1(self):
        return self.__x1

    @x1.setter
    def x1(self, x1):
        if x1 < 0:
            self.__x1 = 0
        else:
            self.__x1 = x1

    @property
    def x2(self):
        return self.__x2

    @x2.setter
    def x2(self, x2):
        if x2 < 0:
            self.__x2 = 0
        else:
            self.__x2 = x2

    @property
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, y1):
        if y1 < 0:
            self.__y1 = 0
        else:
            self.__y1 = y1

    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, y2):
        if y2 < 0:
            self.__y2 = 0
        else:
            self.__y2 = y2


r = Rectangle(0, 0, 1.0, 1.0)
print(r)
print(r.computeArea())
