
input_file = "Account.txt"
def new_account(path,ID,pw):
	"""Them mot ID-PASS  vao file. """
	f = open(input_file,'a')
	f.write(path +'\n' + ID + '|' + pw + '\n')

def change_pass(path,nID,pw,npw):
	List = []
	List = open(input_file).readlines()
	
	i = List.index(path + "\n")
	List [i+1] = nID + "|" + npw + "\n"
	
	f = open(input_file,'w')
	f.writelines(List)
	f.close
	print "Done!"

print "---ACCOUNT MANAGER---:"
print """
	 	1.Hien danh sach account.
	 	2.Thay doi pass word.
	 	3.Them account.
	 	4.Thay doi mat khau dang nhap.
	 	5.Exit.
	 	Moi ban chon chuc nang tuong ung.
	
"""
	
while True:

	x = int(raw_input(">>>>   "))

	if x == 1:
		print open(input_file).read()
		
	if x == 2:
		print "Nhap vao trang web muon doi mat khau:"
		path = raw_input('> ')
		print "Nhap vao ID:"
		nID = raw_input('> ')
		print "Nhap vao mat khau cu: "
		pw = raw_input('> ')
		print "Nhap vao mat khau moi: "
		npw = raw_input('> ')
		change_pass(path,nID,pw,npw)
		
		
	if x == 3:
		print "Nhap vao link cua account"
		link = raw_input('>')
		print "Nhap vao ID"
		ID = raw_input('>')
		print "Nhap vao pass word"
		pass_w = raw_input('>')
		
		new_account(link, ID, pass_w)
		
		print "Da ghi ID - PASS vao %s!" %input_file	
	
	#if x == 4:
		#None
	
	if x == 5: 
		break
	
	if x  > 5 or x < 1:
		print " Khong co chuc nang!!"
		continue

