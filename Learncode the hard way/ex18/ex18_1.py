#from sys import argv
def coppy_file(infile,outfile):
	data = open(infile).read()
	out_file = open(outfile,'w')
	out_file.write(data)

in_p = raw_input("Nhap vao file goc: " )
out = raw_input("Nhap vao file xuat: " )
coppy_file(in_p,out)
print "ND da ghi vao file la : "
print open(in_p).read()