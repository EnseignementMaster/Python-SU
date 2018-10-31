# define cosine function 
import pylab as pl
import numpy as np
import math

debut = -2 * math.pi
fin = 2 * math.pi

pas = 0.1
x = np.arange(debut, fin, pas)
y = np.cos(x)
# draw the plot 
pl.plot(x, y)
pl.xlabel('angle (rad)')
pl.ylabel('cos(angle)')
pl.title('Fonction: y = cos(x)')
pl.grid()
pl.savefig('cos.pdf')
pl.show()
