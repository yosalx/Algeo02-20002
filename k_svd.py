import numpy as np
import ata_methods

def k_svd(matrix,percent): # Melakukan aproksimasi terhadap matriks gambar berdasarkan k dari input user
    # U,Sig,Vt = np.linalg.svd(matrix) 
    U,Sig,Vt = ata_methods.find_svd(matrix) # melakukan dekomposisi terhadap matriks dengan metode svd
    n = np.linalg.matrix_rank(matrix)
    # print("u\n", U.shape)
    # print("Sig\n", Sig.shape)
    # print("Vt\n", Vt.shape)
    
    # mengaproksimasi matriks hasil svd berdasarkan input persentase dari user
    k = percent*n//100 # menghitung banyaknya singular value yg akan digunakan berdasarkan input persentase
    
    # aproksimasi
    min_mat = np.dot(U[:,:k], np.dot(np.diag(Sig[:k]), Vt[:k,:])) 
    
    return min_mat #mengembalikan matriksnya

