from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def  rewind(f):
	f.seek(0)
# Dua con tro ve vi tri dau tien (0) de thuc thi ham tiep theo

def print_a_line(line_count,f):
	print line_count, f.readline()

curren_file = open(input_file)

print "First let's print the whole file:\n"

print_all(curren_file)

print "Now let's rewind, kind of like a tape."

rewind(curren_file)

print "Let's print three lines:"

curren_line = 1
print_a_line(curren_line, curren_file)

curren_line = curren_line + 1
print_a_line(curren_line, curren_file)

curren_line += 1
print_a_line(curren_line, curren_file)
