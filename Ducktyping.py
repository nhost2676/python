class Person():
	def say(self):
		print ("Hello World!")
def quackquck(duck):
	duck.say()

person = Person()
quackquck(Person)

print person.say()
print quackquck