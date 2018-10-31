def myfunction():
    global x
    x = x + 1


x = 3
print(id(x))
myfunction()
print(x)
print(id(x))
