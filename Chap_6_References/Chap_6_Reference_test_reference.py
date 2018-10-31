x = [1, 2, 3]
y = list(x)  # on cree une nouvelle liste
print(id(x))
print(id(y))
y[0] = -999
print(y[0], "\t", x[0])
