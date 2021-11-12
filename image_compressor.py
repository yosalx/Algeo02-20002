import image_processing
import k_svd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def img_comp(filename,k): # parameter input adalah nama file dan jumlah singular value yang akan digunakan
    
    # mengubah gambar yang akan dikompres menjadi matriks, dipisahkan menjadi matriks rgb
    # mengambil ukuran matriks
    n,r,g,b = image_processing.image_matrix(filename) 
    
    comppresed = [] # menyiapkan tempat untuk matriks rgb dari gambar yang akan disederhanakan dengan proses svd
    
    comppresed.append(k_svd.k_svd(r,k)) # menambahkan matriks r sederhana 
    comppresed.append(k_svd.k_svd(g,k)) # menambahkan matriks g sederhana
    comppresed.append(k_svd.k_svd(b,k)) # menambahkan matriks b sederhana

    def merge_rgb(shape,mat): # deklarasi fungsi untuk penggabungan kembali matriks rgb
        merge = np.zeros(shape) # menyiapkan matriks 0 dengan ukuran sesusai ukuran matriks dari gambar
        for i in range(3):
            merge[:,:,i] = mat[i] # menggabungkan matriks rgb
    
        return merge
    
    merge_pic = merge_rgb(n,comppresed) # menggabungkan matriks rgb

    # Untuk test bisa make matplotlib
    # Di uncomment aja
    # plt.imshow(merge_pic.astype(np.uint8))
    # plt.show()
    
    save = Image.fromarray(merge_pic.astype(np.uint8))
    save.save("4k-100.jpg")


# img_comp("tes.jpg", 20)

from datetime import datetime
start_time = datetime.now()	
img_comp("4k.jpg", 100)
end_time = datetime.now()
print('Duration pake qr gilang 6 iterasi: {}'.format(end_time - start_time))