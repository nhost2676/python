class Animal:
	def __init__(self, genus, age):
		self.genus = genus
		self.age = age

	def say(self):
		pass

class Duck(Animal): #Lop Duck duoc khai bao ke thua lop Animal
	def __init__(self):
		#Phuong thuc __init__ duoc ghi de (override) o lop cha Animal
		Animal.__init__(self, 'Dog', 10)
		#Cach de goi mot phuong thuc tu lop cha
	def say(self):
		# Phuong thuc say duoc override lai tu phuong thuc say o lop cha
		print "Quack quack !"
	def __fly(self): # private fly (__abc)
		print "Flap Flap!!!"
	def fly(self):
		print "Bay len nao!!!"
duck1 = Duck()
duck1.fly()

duck = Duck()
duck.__fly()

