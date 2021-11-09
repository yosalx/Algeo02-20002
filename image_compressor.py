import image_processing
import k_svd
import numpy as np


def img_comp(filename,percent):
    
    # mengubah gambar yang akan dikompres menjadi matriks, dipisahkan menjadi matriks rgb
    # mengambil ukuran matriks
    n,r,g,b = image_processing.image_matrix(filename) 
    
    comppresed = [] # menyiapkan tempat untuk matriks rgb dari gambar yang akan disederhanakan dengan proses svd
    
    comppresed.append(k_svd.k_svd(filename,r,percent)) # menambahkan matriks r sederhana 
    comppresed.append(k_svd.k_svd(filename,g,percent)) # menambahkan matriks g sederhana
    comppresed.append(k_svd.k_svd(filename,b,percent)) # menambahkan matriks b sederhana

    def merge_rgb(shape,mat): # deklarasi fungsi untuk penggabungan kembali matriks rgb
        merge = np.zeros(shape) # menyiapkan matriks 0 dengan ukuran sesusai ukuran matriks dari gambar
        for i in range(3):
            merge[:,:,i] = mat[i] # menggabungkan matriks rgb
    
    merge_rgb(n,comppresed) # menggabungkan matriks rgb
    
    return merge_rgb

# Untuk test bisa make matplotlib
# plt.imshow(merge_rgb.astype(np.uint8))

