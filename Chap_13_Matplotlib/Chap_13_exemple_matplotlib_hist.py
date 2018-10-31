# define cosine function 
import matplotlib.pyplot as plt
import random

x=[]
y=[]
for i in range(10000):
	x.append(i)
	y.append(random.uniform(0,1))

print(y)
# draw the plot 
plt.hist(y)

plt.show()