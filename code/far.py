filein = "test.txt"
f = open(filein,'r')
filedata = f.read()
f.close()
old_data = "naht"
new_data = "nhat"
newdata = filedata.replace(old_data,new_data)

f = open(filein,'w')
f.write(newdata)
f.close()