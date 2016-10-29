#X = Y = K =1
#N = 2
#A = []
#B = []
#[A.append([i, j, k]) for i in range (X +1 ) for j in range(Y + 1) for k in range(K + 1) if i + j + k != N ]
#
#print A
#for i in range(X + 1):
#	for j in range(Y + 1):
#		for k in range(K + 1):
#			if i + j + k != N:
#				B.append([i,j,k]) 
#
#print B
x = [1,1,4,5,7,7,8,9,8,4,0]
def soft(arr):
	return list(set(arr))

print soft(x)