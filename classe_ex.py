# ESEMPIO DI UTILIZZO DI UNA CLASSE

class ProvaUno(object):
	
	
	def __init__(self,a):
		self.la = a

	def perimetro(self):
		return (self.la * 4)

	def area(self):
		return (self.la * self.la)

d=ProvaUno(2)

print("Perimetro: ", d.perimetro())
print("Area: ", d.area())
#print(d.perimetro())	
