from pylab import *


# ===========================================
def Dessin(event):
    x, y = event.xdata, event.ydata  # recupere position de la souris
    print("x=", x, " y=", y)
    if (event.button == 1):  # si clique gauche (ou 2,3 : milieu,droit) # dessine un rond rouge en x,y :
        plot([x], [y], marker='o', markersize=10, c='r')
        draw()


# ===============================================

axis([0, 1, -2, 2])  # domaine des coordonnees
# ---dessin de lignes----
x1, y1, x2, y2 = 0, -2, 1, 2  # coordonnees des extremites
plot([x1, x2], [y1, y2], c='b')  # dessin d'une ligne
xlabel("$x$")  # titre des axes
ylabel("$y$")
title("Cliquez")
connect('button_press_event', Dessin)  # la fonction Dessin sera appelee si la souris est cliquee
show()
