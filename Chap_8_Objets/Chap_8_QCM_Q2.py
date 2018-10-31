
class D(object):
    def __init__(self, a=None, b=None):

        if a:
            if b:
                self.__init__(b)
                self.x -= a
            else:
                self.__init__()
                self.x += a
        else:
            self.x=3

a = D(5,6)
print(a.x)