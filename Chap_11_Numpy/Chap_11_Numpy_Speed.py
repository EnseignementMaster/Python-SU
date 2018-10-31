import numpy as np
import time

# A = np.ones((10000, 10000), order='F')
t0 = time.time()
n = 5000
A = np.arange(n * n)
# print "A=", A
A.resize(n, n)
# print A
b = np.arange(n)
b.resize(1, n)
# print b

x = np.dot(A, b.transpose())
# print x
timeNP = time.time() - t0

t0 = time.time()
B = range(n * n)
A = []
for i in range(n):
    A.append(B[i * n:(i + 1) * n])
b = range(n)

x = []
for i in range(n):
    temp = 0
    for j in range(n):
        temp += A[i][j] * b[j]
    x.append(temp)
# print x

timeList = time.time() - t0

print("time Numpy=", timeNP, "time List", timeList, "ratio", timeList / timeNP)
#

# for i in range(10000):
#  A[:,i] *= 2.0 # scaling each column

# print time.time()-t0 # 0.119 second

# t0 = time.time()
# for i in range(10000):
#  A[i, :]*= 2.0 # scaling each row

# print time.time()-t0 # 1.574 seconds
