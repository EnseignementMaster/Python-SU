import numpy as np
import time

A = np.ones((10000, 10000), order='F')

t0 = time.time()

for i in range(10000):
  A[:,i] *= 2.0 # scaling each column

print(time.time()-t0) # 0.119 second

t0 = time.time()
for i in range(10000):
  A[i, :]*= 2.0 # scaling each row

print(time.time()-t0) # 1.574 seconds
