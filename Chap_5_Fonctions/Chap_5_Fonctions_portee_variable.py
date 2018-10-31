x = 10
print(id(x))


def hello(prenom, x):
    print("hello", id(x))
    print("Bonjour ", prenom)
    x = x + 1
    print("hello, x+1", id(x))
    x = 42
    print("hello, x=42", id(x))
    print("hello", x)


hello("Patrick", x)
print("global", x)
print(id(x))
