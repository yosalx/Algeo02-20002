import numpy as np
import ata_methods

def k_svd(matrix,percent): # Melakukan aproksimasi terhadap matriks gambar berdasarkan k dari input user
    # U,Sig,Vt = np.linalg.svd(matrix) 
    U,Sig,Vt = ata_methods.find_svd(matrix) # melakukan svd terhadap matriks
    n = len(Sig)
    # print("u\n", U.shape)
    # print("Sig\n", Sig.shape)
    # print("Vt\n", Vt.shape)
    
    # mengaproksimasi matriks hasil svd berdasarkan input k
    k = percent*n//100
    min_mat = np.dot(U[:,:k], np.dot(np.diag(Sig[:k]), Vt[:k,:]))
    
    return min_mat #mengembalikan matriksnya

