import numpy as np
import math
import qr_decomposition
import numpy as np

def find_svd(a): # dekomposisi matriks 
    def find_v(matrix): # fungsi untuk membuat matriks singular kanan (v) dari matriks persegi panjang
        a = matrix
        at = a.transpose()
        v = np.dot(at,a)
        return v
    v = find_v(a)
    rows = len(a)
    cols = len(a[0])
    
    # pake qr decomposition method 
    # untuk nyari eigen value dan vector dari matriks persegi v
    eval,evec = qr_decomposition.find_eig_qr(v) 
    
    # pake library eigen
    # eval,evec = np.linalg.eig(v)
    
    eigenValues = eval
    eigenVectors = evec
    idx = eigenValues.argsort()[::-1]   
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]
    
    n = len(eigenValues)
    singular = np.zeros(n)
    for i in range(n):
        if (eigenValues[i] < 1e-16):
            singular[i] = 0
        else:
            singular[i] = math.sqrt(eigenValues[i])
    
    #print((-1) * eigenVectors.transpose())
    vT = (-1) * eigenVectors.transpose()
    #v = (-1) * eigenVectors

    matrixs = np.zeros((rows,cols))
    for i in range(np.linalg.matrix_rank(a)):
        matrixs[i][i] = math.sqrt(eigenValues[i])

    matu = np.zeros((rows,rows))
    for j in range(rows):
        matu[:,j] = (np.matmul(a,vT[j])) / math.sqrt(abs(eigenValues[j]))
    return matu,singular,vT