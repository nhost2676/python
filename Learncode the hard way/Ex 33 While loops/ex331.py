def func(n, step):
	number = []

	for i in range(0,n,step):
		print "At the top i is %d" % i
		number.append(i)

		i = i + step
		print "Number now: ", number
		print "At the bottom i is %d" % i

	print "The numbers: "
	
	for num in number:
		print num

n = int(raw_input('Nhap n >>> '))
func(n,5)