import numpy as np
import math
import qr_decomposition
import numpy as np


def find_v(matrix): # return matriks singular kanan (v) dari matriks persegi panjang
    matrix_t = matrix.transpose()
    v = np.dot(matrix_t,matrix)
    return v
    
def find_svd(a): # dekomposisi matriks 
    v = find_v(a)
    rows = len(a)
    # cols = len(a[0])
    
    # pake qr decomposition method 
    # untuk nyari eigen value dan vector dari matriks persegi v
    eval,evec = qr_decomposition.find_eig_qr(v) 
    
    # test pake library eigen
    # eval,evec = np.linalg.eig(v)
    
    
    eigenValues = eval
    eigenVectors = evec
    
    # mengurutkan dalam descending order
    idx = eigenValues.argsort()[::-1]   
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]
    
    # sigma
    singular = np.zeros(len(eigenValues))
    for i in range(len(eigenValues)):
        if (eigenValues[i] < 1e-16):
            singular[i] = 0
        else:
            singular[i] = math.sqrt(eigenValues[i])
    
    #print((-1) * eigenVectors.transpose())

    # v transpose
    vT = eigenVectors.transpose()

    # matriks persegi singular kiri U
    matu = np.zeros((rows,rows))
    for j in range(rows):
        matu[:,j] = (np.matmul(a,vT[j])) / math.sqrt(abs(eigenValues[j]))
    
    return matu,singular,vT