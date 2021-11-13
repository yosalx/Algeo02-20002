import numpy as np
import math
import qr_decomposition
import numpy as np

def find_v(matrix):
    a = matrix
    at = a.transpose()
    v = np.dot(at,a)
    return v

def find_svd(a):
    v = find_v(a)
    rows = len(a)
    cols = len(a[0])
    
    # pake qr method Gilang
    eval,evec = qr_decomposition.find_eig_qr(v) 
    
    # pake library eigen
    # eval,evec = np.linalg.eig(v)
    
    idx = eval.argsort()[::-1]   
    eval = eval[idx]
    evec = evec[:,idx]
    n = len(eval[eval != 0.0])
    
    singular = np.zeros((n, n))
    singular[:n, :n] = np.diag(eval)
    
    # for i in range(n):
    #     if (eval[i] < 1e-16):
    #         singular[i] = 0
    #     else:
    #         singular[i] = math.sqrt(eigenValues[i])
    
    #print((-1) * eigenVectors.transpose())
    vT = (-1) * evec.transpose()
    #v = (-1) * eigenVectors

    matu = np.zeros((rows,rows))
    rank = np.linalg.matrix_rank(a)
    for j in range(rank):
        matu[:,j] = (np.matmul(a,vT[j])) / math.sqrt(abs(eval[j]))
    return matu,singular,vT