import image_processing
import k_svd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import math

def img_comp(filename,percent): # parameter input adalah nama file dan jumlah singular value yang akan digunakan
    
    # mengubah gambar yang akan dikompres menjadi matriks, dipisahkan menjadi matriks rgb
    # mengambil ukuran matriks
    n,r,g,b = image_processing.image_matrix(filename) 
    
    comppresed = [] # menyiapkan tempat untuk matriks rgb dari gambar yang akan disederhanakan dengan proses svd
    
    r = np.clip((k_svd.k_svd(r,percent)),0,255) # mengaproksimasi 
    g = np.clip((k_svd.k_svd(g,percent)),0,255) # menambahkan matriks g sederhana
    b = np.clip((k_svd.k_svd(b,percent)),0,255) # menambahkan matriks b sederhana

    comppresed.append(r)
    comppresed.append(g)
    comppresed.append(b)
    
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
    save = save.convert('RGB')
    # save.save('{}converted'.format(filename))
    savename,ext = os.path.splitext(filename)
    savename = f'{savename}Compressed'
    save.save(f'{savename}{ext}')
    
    
    # plt.imshow(save)
    # plt.show()

def pixel_diff(filename,percent):
    im = Image.open(filename)
    matrix = np.asarray(im).astype(float)
    n = np.linalg.matrix_rank(matrix)
    k = percent*n//100
    
    diff = int(math.ceil((k/100)*((1+im.size[0]+im.size[1])/(im.size[0]*im.size[1]))))
    
    return diff
    
# img_comp("tes.jpg", 20)

# from datetime import datetime
# start_time = datetime.now()	
# # img_comp("tes2.jpg", 50)
# end_time = datetime.now()
# duration = end_time - sta
# print('Duration pake qr gilang 6 iterasi: {}'.format(end_time - start_time))

