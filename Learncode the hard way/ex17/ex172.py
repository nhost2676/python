from sys import argv
from os.path import exists

path, from_file, to_file = argv
#
#data = open(from_file).read()
#out_file = open(to_file, 'w')
#out_file.write(data)

#
#print"Noi dung trong %s la : \n " %to_file
#print open(to_file).read()
#****************************************

open(to_file,'w').write(open(from_file).read())
print open(to_file).read()

# vi file out da ton tai nen khong can dung close