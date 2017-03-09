# Multiplication of two square matrices using Recursion

A = [[1, 2, 3, 4],
 	[5, 6, 7, 8], 
 	[9, 10, 11, 12],
 	[13,14, 15, 16]]
 	 
B = [[1, 0, 0, 0], 
	[0, 1, 0, 0],
 	[0, 0, 1, 0], 
 	[0, 0, 0, 1]]

# A = np.matrix(1)
# B = np.matrix(2)
# C = np.matrix(3)
# D = np.matrix(4)

# print A*B
# print C*D
# print A*B + C*D

def split(A):
	n = len(A)
	P = []
	Q = []
	R = []
	S = []
	for i in range(n/2):
		temp = []
		for j in range(n/2):
			temp.append(A[i][j])
		P.append(temp)

	for i in range(n/2):
		temp = []
		for j in range(n/2, n, 1):
			temp.append(A[i][j])
		Q.append(temp)

	for i in range(n/2, n, 1):
		temp = []
		for j in range(n/2):
			temp.append(A[i][j])
		R.append(temp)

	for i in range(n/2, n, 1):
		temp = []
		for j in range(n/2, n, 1):
			temp.append(A[i][j])
		S.append(temp)


	return P, Q, R, S

def combine(A, B, C, D):
	l = [A, B, C, D]
	return_matrix = []
	n = len(A)
	temp = []
	for i in range(2):
		for j in range(n):
			temp2 = A[j][:] + B[j][:]
			temp.append(temp2)
		A[:] = C[:]
		B[:] = D[:]
	return temp

def add(A, B):
	for i in range(len(A)):
		for j in range(len(A)):
			A[i][j] += B[i][j]

	return A


def matrix_multiply(P, Q):
	temp = []
	n = len(P)/2
	if n < 1:
		return [[P[0][0]*Q[0][0]]]

	A, B, C, D = split(P)
	E, F, G, H = split(Q)

	X1 = matrix_multiply(A, E)
	Y1 = matrix_multiply(B, G)

	X2 = matrix_multiply(A, F)
	Y2 = matrix_multiply(B, H)

	X3 = matrix_multiply(C, E)
	Y3 = matrix_multiply(D, G)

	X4 = matrix_multiply(C, F)
	Y4 = matrix_multiply(D, H)

	sum1 = add(X1,Y1)
	sum2 = add(X2,Y2)
	sum3 = add(X3,Y3)
	sum4 = add(X4,Y4)

	return combine(sum1, sum2, sum3, sum4)

# A, B, C, D = split(B)

# A, B, C, D = split(A)

# print A, B
# print add(A, B)

print matrix_multiply(A, B)
# A = [[1, 2], [5, 6]]
# B = [[3, 4], [7, 8]]
# C = [[9, 10], [13, 14]]
# D = [[11, 12], [15, 16]]
# # print combine(A, B, C, D)

