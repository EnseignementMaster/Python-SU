from pylab import *
# Import Ellipse and Wedge to current namespace 
from matplotlib.patches import Ellipse, Wedge  # a list of some patches

my_patches = [
    Arrow(0, 4, 0, -4, facecolor='g'),
    Circle([-2, 2], 1.5, linewidth=4, fc='orange'),
    Ellipse([2, 3], 4, 1, 45.0, edgecolor='r'),
    Polygon([[4, 2], [3, 3], [1, -1], [3, -1]], ls='dashed', fill=False),
    Polygon([[4, 2], [5, -1], [3, -1]], ls='dashed', fill=False),
    Wedge([-1, 0], 3, 200, 300, fc='m', ec='m'),
    Rectangle([1, -2], 3, -2, fill=False, lw=5, ec='r')
]
# draw a figure 
figure()
axis([-5, 5, -5, 5])  # add the patches
cur_ax = gca()
print(len(my_patches))
for p in my_patches:
    cur_ax.add_patch(p)

title('Patches')
show()
