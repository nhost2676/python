print "Chuong trinh ghi file"

def ghi(f,data):
	txt = open(f,'w')
	txt.write(data)
	txt.close()

print "Nhap vao ten file"
file = raw_input(">>>")
print "Nhap noi dung moi can ghi"
data = raw_input(">>>")
ghi(file,data)
print "Da ghi xong! Du lieu da ghi vao la :"
print open(file).read()