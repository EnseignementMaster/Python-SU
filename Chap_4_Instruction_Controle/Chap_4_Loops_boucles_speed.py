import time

# creation d'une liste de 5 000 000 d'elements 
# (a adapter suivant la vitesse de vos machines) 
taille = 10000000
print("Creation d'une liste avec %d elements" % (taille))
toto = list(range(taille))
# la variable 'a' accede a un element de la liste
# methode 1 
start = time.time()
for i in range(len(toto)):
    a = toto[i]
print("methode 1 (for in range) : %.1f secondes" % (time.time() - start))

# methode 2
start = time.time()
for ele in toto:
    a = ele
print("methode 2 (for in) : %.1f secondes" % (time.time() - start))

# methode 3
start = time.time()
for idx, ele in enumerate(toto):
    a = ele
print("methode 4 (for in enumerate): %.1f secondes" % (time.time() - start))
