import copy


class Point(object):
    def __init__(self, x, y):
        self.coord = [x, y]

    def __repr__(self):
        return "(" + str(self.coord[0]) + ", " + str(self.coord[1]) + ")"


a = Point(5, 2)
b = copy.copy(a)
print("a= ", a, "b= ", b)
b.coord[0] = 2;
print("a= ", a, "b= ", b)
a.coord[0] = 2;
if a == b:
    print("Egaux!")
else:
    print("Inegaux!")
