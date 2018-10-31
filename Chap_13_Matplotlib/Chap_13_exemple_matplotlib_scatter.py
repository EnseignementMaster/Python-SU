# define cosine function 
import pylab as pl
import math
import random

x=[]
y=[]
for i in range(10):
    x.append(random.uniform(-1,1))
    y.append(random.uniform(-1,1))
    
# draw the plot 
pl.scatter(x,y, c='k', marker='o')

pl.show()