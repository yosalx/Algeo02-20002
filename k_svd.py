import svd
import numpy as np
from PIL import Image
import math

def k_svd(matrix,k): # Melakukan aproksimasi terhadap matriks gambar berdasarkan k dari input user
    U,Sig,Vt = np.linalg.svd(matrix) # melakukan svd terhadap matriks
    
    # mengaproksimasi matriks hasil svd berdasarkan input k
    min_mat = np.dot(U[:,:k], np.dot(np.diag(Sig[:k]), Vt[:k,:]))
    
    return min_mat #mengembalikan matriksnya