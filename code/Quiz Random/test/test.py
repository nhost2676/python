from random import randrange
f = open("in.txt")
li = f.readlines()
li = map(lambda s : s.strip(), li)
print li

index = randrange(0, len(li))
print index

if index % 2 != 0:
	print  li[index - 1]
	aw = raw_input(">>>> ")
	if aw == li[index]:
		print "RIGHT!!!!"
	else:
		print "WRONG!!"
else:
	print li[index]
	aw = raw_input(">>>> ")
	if aw == li[index + 1]:
		print "RIGHT!!!!"
	else:
		print "WRONG!!"
