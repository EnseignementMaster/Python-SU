import numpy as np

a = np.linspace(1, 5, 5)
print("a= ", a)
b = a
print("b= ", b)
c = a.copy()
print("c= ", c)
d = np.zeros(a.shape, a.dtype)
d[:] = a
print("d= ", d)

b[1] = 9
print('\n')
print("a= ", a)
print("b= ", b)
print("c= ", c)
print("d= ", d)

e = np.dot(d.T, d)
print(e)

A = np.eye(2)
A[0][0] = 2.0
A[0][1] = 2.0

print("A= ", A)

B = np.eye(2)
B = 2 * B
B[0, 1] = 1.0
print("B= ", B)

C = np.dot(A, B)
print("C= ", C)
