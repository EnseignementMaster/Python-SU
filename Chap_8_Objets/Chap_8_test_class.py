__author__ = 'lantos'


class B(object):

    def __init__(self, i=0):
        self.__i = i
        if i:
            self.__init__()
            print("Bonjour", self.__i, )
        else:
            print("Salut", )


B(2003)
