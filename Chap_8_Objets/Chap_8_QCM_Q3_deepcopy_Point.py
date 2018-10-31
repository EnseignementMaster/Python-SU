import copy

class Point(object):
    def __init__(self, x, y):
        self.coordinate = [x,y]

    def __repr__(self):
        return "(" + str(self.coordinate[0])+ ", "+ str(self.coordinate[1])+ ")"


a = Point(5, 2)
print( id(a.coordinate))
b = copy.deepcopy(a)
print( id(b.coordinate))
print( "a= ",a,  "b= ", b)
b.coordinate[0] = 2;
print( "a= ",a,  "b= ", b)
a.coordinate[0] = 2;
if a == b:
    print( "Egaux!")
else:
    print( "Inegaux!")


