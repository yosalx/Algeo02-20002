import svd
import numpy as np
from PIL import Image

def k_svd(filename,matrix,percent):
    U,Sig,Vt = svd(matrix) # melakukan svd terhadap matriks
    
    # Mencari nilai singular value yang akan digunakan berdasarkan persentase yang diinginkan
    im = Image.open(filename) 
    k = ((im.size[1]*im.size[0])/(im.size[1]+im.size[0]))*(percent/100)
    
    #menyederhanakan matriks hasil svd berdasarkan input k
    min_mat = np.dot(U[:,:k], np.dot(np.diag(Sig[:k]), Vt[:k,:]))
    
    return min_mat #mengembalikan matriksnya
    