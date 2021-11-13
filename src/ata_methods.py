import numpy as np
import math
import qr_decomposition
import numpy as np

def find_v(matrix):  # return matriks persegi singular kanan V dari matriks persegi panjang
    a = matrix
    at = a.transpose()
    v = np.dot(at,a)
    return v

def find_svd(a):
    v = find_v(a) # matriks V dari dekomposisi matriks persegi panjang a
    rows = len(a) # ambil panjang baris matriks a
    #cols = len(a[0]) # ambil panjang kolom matriks a
    
    # return eigen value dan eigen vector dari matriks persegi v dengan metode dekomposisi QR
    eval,evec = qr_decomposition.find_eig_qr(v) 
    
    # test pake library eigen
    # eval,evec = np.linalg.eig(v)
    
    # sort eigen value dan eigen vector dalam descending order
    idx = eval.argsort()[::-1]   
    eval = eval[idx] 
    evec = evec[:,idx]
    
    n = len(eval)
    singular = np.zeros(n)
    # mengisi nilai singular matriks dari akar eigen value
    for i in range(n):
        if (eval[i] < 1e-16):
            singular[i] = 0
        else:
            singular[i] = math.sqrt(eval[i])
    
    #print((-1) * evec.transpose())
    vT = (-1) * evec.transpose() # mencari matriks persegi Vtranspose
    #v = (-1) * evec

    # mencari matriks persegi U
    matu = np.zeros((rows,rows)) 
    rank = np.linalg.matrix_rank(a)
    
    # mengisi matriks u dari rumus Ui = AVi/Si
    for j in range(rank):
        matu[:,j] = (np.matmul(a,vT[j])) / math.sqrt(abs(eval[j]))
    return matu,singular,vT