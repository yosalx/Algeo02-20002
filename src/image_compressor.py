import image_processing
import image_processing2
import k_svd
import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image
import os

def img_comp(filename,percent): # parameter input adalah nama file dan jumlah singular value yang akan digunakan
    
    # mengubah gambar yang akan dikompres menjadi matriks, dipisahkan menjadi matriks rgb
    # mengambil ukuran matriks
    n,r,g,b = image_processing.image_matrix(filename) 
    
    comppresed = [] # menyiapkan tempat untuk matriks rgb dari gambar yang akan disederhanakan dengan proses svd
    
    r = np.clip((k_svd.k_svd(r,percent)),0,255) # mengaproksimasi matriks r
    g = np.clip((k_svd.k_svd(g,percent)),0,255) # mengaproksimasi matriks g
    b = np.clip((k_svd.k_svd(b,percent)),0,255) # mengaproksimasi matriks b

    comppresed.append(r) # menambahkan matriks r sederhana
    comppresed.append(g) # menambahkan matriks g sederhana
    comppresed.append(b) # menambahkan matriks b sederhana
    
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
    
def img_comp_png(filename,percent):
    
    # mengubah gambar yang akan dikompres menjadi matriks, dipisahkan menjadi matriks rgba
    r,g,b,alp = image_processing2.image_matrix2(filename)
    
    r = np.clip((k_svd.k_svd(r,percent)),0,255) # mengaproksimasi matriks r
    g = np.clip((k_svd.k_svd(g,percent)),0,255) # mengaproksimasi matriks g
    b = np.clip((k_svd.k_svd(b,percent)),0,255) # mengaproksimasi matriks b
    
    #mengubah matriks menjadi bentuk gambar dalam mode grayscale (convert("L"))
    r_im = (Image.fromarray(r)).convert("L")
    g_im = (Image.fromarray(g)).convert("L")
    b_im = (Image.fromarray(b)).convert("L")
    alp_im = (Image.fromarray(alp)).convert("L")
    
    save_png = Image.merge("RGBA", (r_im,g_im,b_im,alp_im)) # menggabungkan kembali keempat gambar dari keempat array sebelumnya dengan mode RGBA
    save_png.save("savepng.png")

#img_comp_png("src/test_png.png",80)
# img_comp("tes.jpg", 20)

# from datetime import datetime
# start_time = datetime.now()	
# # img_comp("tes2.jpg", 50)
# end_time = datetime.now()
# duration = end_time - sta
# print('Duration pake qr gilang 6 iterasi: {}'.format(end_time - start_time))

