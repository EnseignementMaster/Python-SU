class A(object): #Convention: un objet commence par une majuscule

	def __init__(self, x, y):  # initialisation (remplace le constructeur)
		# Noter le self
		__x = x  # pour l'instant x et y sont accessibles
		__y = y  # de l'exterieur: public

	def addX(self, dx):
		__x = __x + dx

	def __str__(self):
		return str(__x) + " , " + str(__y)


a = A(1.0, 2.0)
a.addX(2.0)
print(a)
