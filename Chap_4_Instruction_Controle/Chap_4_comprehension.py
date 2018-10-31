__author__ = 'lantos'

L = range(20)
liste = [i for i in L[::-3] if i % 2 == 0]
print(liste)
