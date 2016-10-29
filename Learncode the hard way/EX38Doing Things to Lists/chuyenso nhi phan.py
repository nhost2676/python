a = int(raw_input("Nhap so nguyen can chuyen doi: "))
k = []

while a > 0:
    n = int(float(a%2))
    k.append(n)
    a = (a - n)/2

k.append(0)
string = ""
for j in k[::-1]:
    string = string + str(j)
print "So nhi phan la: ", string
print k