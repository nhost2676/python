input_file = "Account.txt"
List = []
List = open(input_file).readlines()
print List
path = raw_input(">>> ")
nID = raw_input(">>> ")
nps = raw_input(">>> ")

i = List.index(path + "\n")
List [i+1] = nID + "|" + nps + "\n"
f = open(input_file,'w')
f.writelines(List)
f.close()