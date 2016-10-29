def Question():
	print "Ai la nguoi dep trai nhat?"
	as1 = raw_input('>>> ')
	print "2 + 2  = "
	as2 = raw_input('>>> ')
	print "3 * 5 = "
	as3 = raw_input('>>> ')

	if as1 == "Nam" and as2 == "4" and as3 == "15":
		print "Ban se duoc dua den Gold room!!!"
		#Gold_room()
	else:
		start()

def Monter_room():
	print "Nham mat lai va go dong chu dau: 'Anh Nam Dep trai' "
	ip = raw_input('>>> ')

	if ip == 'Anh Nam Dep trai':
		#Gold_room()
		print "You win!!"
	else:
		start()

def start():
	print """
		Ban nhin thay hai canh cua
		Ban hay chon 1 or 2
	"""
	choice = raw_input('>>>> ')

	if choice == '1':
		Question()
	elif choice == '2':
		Monter_room()
	else:
		start()

start()