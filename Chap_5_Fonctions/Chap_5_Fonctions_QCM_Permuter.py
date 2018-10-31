def permuter(s1, s2, x1, x2):
    print("\nCall of permuter")
    print(id(s1), id(s2), id(x1), id(x2))
    tmp1 = s1
    s1 = s2
    s2 = tmp1
    tmp1 = x1
    x1 = x2
    x2 = tmp1
    print(id(s1), id(s2), id(x1), id(x2))


a = "bon"
b = "jour"
c = 3
d = 4
print(id(a), id(b), id(c), id(d))
permuter(a, b, c, d)
print(a, b, c, d)

a = ["bon"]
b = ["jour"]
c = [3]
d = [4]

permuter(a, b, c, d)
print(a, b, c, d)
