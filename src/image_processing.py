import numpy as np
from PIL import Image

def image_matrix(filename): 
    im = np.asarray(Image.open(filename)).astype(float) # Mengubah data dari gambar menjadi bentuk array 3 dimensi
    
    # Memisahkan array pada dimensi ke 3 nya, shape dari array im adalah (x,x,3)
    # 0 mewakili r, 1 mewakili g, 2 mewakili b
    red_im = im[:,:,0]
    green_im = im[:,:,1]
    blue_im = im[:,:,2]
    
    #mengembalikan ukuran array dan ketiga rgb based array
    return im.shape,red_im, green_im, blue_im 

    
