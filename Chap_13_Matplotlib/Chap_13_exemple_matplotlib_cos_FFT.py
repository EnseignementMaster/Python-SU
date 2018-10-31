from pylab import *

# define cosine function
x = arange(-2 * pi, 2 * pi, 0.1)
y = cos(x)

# calculate TF of cosine function 
TF = fft(y)
ABSTF = abs(TF)
pas_xABSTF = 1 / (4 * pi)
x_ABSTF = arange(0, pas_xABSTF * len(ABSTF), pas_xABSTF)

# draw cos plot 
plot(x, y)
xlabel('angle (rad)')
ylabel('cos(angle)')
title('Fonction: y = cos(x)')
grid()
show()

# plot TF of cosine 
plot(x_ABSTF[:20], ABSTF[:20])
xlabel('inverse angle (rad^-1)')
ylabel('Intensity')
title('Spectrum of cosine function')
grid()
show()
