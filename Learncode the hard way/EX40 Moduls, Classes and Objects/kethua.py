class hocsinh():
	diem = []
	def __init__(self, name):
		self.name = name
	
	def themdiem(self, d):
		hocsinh.diem.append(d)
	
	def __str__(self):
		st = "Ho va ten: " + self.name + "\nDiem: " 
		for i in hocsinh.diem:
			st += str(i) + ", "
		return st

class hocsinh2(hocsinh):
	def __init__(self, hoten, hocluc):
		hocsinh.__init__(self, hoten)
		self.hocluc = hocluc
	def __str__(self):
		return


hs1 = hocsinh("Name")
hs1.themdiem(10)
hs1.themdiem(15)
print hs1