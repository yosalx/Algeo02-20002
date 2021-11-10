#Edward Harianto
import numpy as np

def isDiagonal(mat):
	for i in range(len(mat)):
		for j in range(len(mat)):
			if(i == j):
				continue
			else:
				if (abs(mat[i][j]) > 0.001):
					return False
	return True

def qrAlgorithm(mat):
	num = 0
	
	while(True):
		q,r = np.linalg.qr(mat)
		mat = np.dot(r,q)
		
		if(isDiagonal(mat)):
			break
		num+=1

	print('QR Factoriztion matrix')
	print(mat)
	print(str(num) + ' iterations')
	
	count = 1
	for i in range(len(mat)):
		for j in range(len(mat)):
			if (i == j):
				print("lambda " + str(count) + ": " + str(mat[i][j]))
				count+=1

def qr_factorization(A):
   #source: http://mlwiki.org/index.php/Gram-Schmidt_Process
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q @ v
            v = v - R[i, j] * q
        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R

def find_eig_qr(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(100):
            Q,R = np.linalg.qr(X)
            pQ = pQ @ Q;
            X = R @ Q;
    return np.diag(X), pQ



A = np.array([[2,0,2],[0,3,0],[2,0,2],[0,3,0],[2,0,2]])
AT = np.transpose(A)
AAT = np.matmul(A,AT)
matrix = np.random.random_integers(0, 100, (1000, 1000))
from datetime import datetime
start_time = datetime.now()	
x,y = find_eig_qr(AAT)

u,Sig,V = np.linalg.svd(A)

print(x)
print("eigenvector")
print(y)
print("svd")
print(u)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

