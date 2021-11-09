import numpy as np
from PIL import Image

def image_matrix(filename): 
    im = np.asarray(Image.open(filename)) # Mengubah gambar menjadi bentuk matrix 3 dimensi
    
    # Memisahkan matriks gambar menjadi matriks rgb 
    red_im = im[:,:,0]
    green_im = im[:,:,1]
    blue_im = im[:,:,2]
    
    #mengembalikan ukuran matriks gambar dan ketiga matriks rgb
    return im.shape,red_im, green_im, blue_im 

    
