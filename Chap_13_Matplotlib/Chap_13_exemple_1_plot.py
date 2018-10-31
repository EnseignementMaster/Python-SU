# define cosine function 
import pylab as pl

X= pl.linspace(-pl.pi, pl.pi, 256, endpoint=True)
C,S = pl.cos(X), pl.sin(X)
pl.plot(X,C)
pl.plot(X,S)
pl.xlim(-5.0, 5.0)
pl.xticks(range(-3,4,2))
pl.ylim(-5.0, 5.0)
pl.show()