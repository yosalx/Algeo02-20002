from functools import singledispatch
import numpy as np
from numpy.core.defchararray import find
from numpy.core.einsumfunc import _find_contraction
from numpy.core.fromnumeric import trace
from numpy.testing._private.utils import print_assert_equal
from datetime import datetime
from PIL import Image

def svd(A):
    At = np.transpose(A)
    AAt = A @ At
    AtA = At @ A

    # finding singular values, V, U
    eigen, V = find_eigen(AtA)
    _, U = find_eigen(AAt)
    print("eigen\n", eigen)
    singular_values = np.sqrt(eigen)
    # print("singular value\n", singular_values)
    Vt = np.transpose(V)

    sigma = np.zeros(A.shape)
    #isi elmt diagonal sigma dengan singular values
    for i in range(A.shape[0]) :
        sigma[i][i] = singular_values[i]

    return U,sigma,Vt,eigen

def reconstruct(U,sigma,Vt):
    return U @ (sigma @ Vt)

def find_eigen(A):
    pQ = np.eye(A.shape[0])       # matrik identitas nxn
    X=A.copy()
    for i in range(100):
            Q,R = np.linalg.qr(X)
            pQ = pQ @ Q;
            X = R @ Q;
    return np.diag(X), pQ

# testcase
# A = np.array([[3,1,1],[-1,3,1]])
# matrix = np.random.random_integers(0, 100, (1000, 1200))

start_time = datetime.now()





im = np.asarray(Image.open("cat.jpg")).astype(float) # Mengubah data dari gambar menjadi bentuk matrix

# Memisahkan matriks gambar menjadi matriks rgb
# 0 mewakili r, 1 mewakili g, 2 mewakili b
red_im = im[:,:,0]
green_im = im[:,:,1]
blue_im = im[:,:,2]

end_time = datetime.now()
U,sigma,V = svd(red_im)
print('Duration: {}'.format(end_time - start_time))
print(U)
print(sigma)
print(V)
