import time
from random import randrange
st = " a b c d e f g h i j k l m n o p q r s t u y v w z 0 1 2 3 4 5 6 7 8 9 A B C E F G H I J K L M N O P Q S T U Y V W Z"
char = st.split(" ")
CD = int(raw_input("Nhap chieu dai: "))
pw = ""
while CD > 0:
	pw  += char[randrange(0,len(char))]
	CD -= 1
print pw
f = open("Pass.txt","a")
f.write(pw + "\n")
f.close()
time.sleep(60)
