print "How old are you?", # neu khong co dau " ,",sau print se xuong hang,#
						# co dau "," de nhap tiep tuc tren cung line voi print
age = raw_input() # gia tri nhap tu ban phim la chuoi, khong phai number
					 #>>chuyen sang number bang int(age) or age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)