import numpy as np

# def isDiagonal(mat):
# 	for i in range(len(mat)):
# 		for j in range(len(mat)):
# 			if(i == j):
# 				continue
# 			else:
# 				if (abs(mat[i][j]) > 0.001):
# 					return False
# 	return True

# def qrAlgorithm(mat):
# 	num = 0
	
# 	while(True):
# 		q,r = np.linalg.qr(mat)
# 		mat = np.dot(r,q)
		
# 		if(isDiagonal(mat)):
# 			break
# 		num+=1

# 	print('QR Factoriztion matrix')
# 	print(mat)
# 	print(str(num) + ' iterations')
	
# 	count = 1
# 	for i in range(len(mat)):
# 		for j in range(len(mat)):
# 			if (i == j):
# 				print("lambda " + str(count) + ": " + str(mat[i][j]))
# 				count+=1

# def qr_factorization(A):
#        #source: http://mlwiki.org/index.php/Gram-Schmidt_Process
#     m, n = A.shape
#     Q = np.zeros((m, n))
#     R = np.zeros((n, n))
#     for j in range(n):
#         v = A[:, j]
#         for i in range(j - 1):
#             q = Q[:, i]
#             R[i, j] = q @ v
#             v = v - R[i, j] * q
#         norm = np.linalg.norm(v)
#         Q[:, j] = v / norm
#         R[j, j] = norm
#     return Q, R

def find_eig_qr(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(6):
            Q,R = np.linalg.qr(X)
            pQ = pQ @ Q;
            X = R @ Q;
    return np.diag(X), pQ