import numpy as np
from PIL import Image
import k_svd

def image_matrix2(filename):
    im = np.asarray((Image.open(filename)).convert("RGBA")).astype(float) # Mengubah data dari gambar menjadi bentuk array t dimensi dengan mode convert RGBA
    
    # Memisahkan array pada dimensi ke 4 nya, shape dari array im adalah (x,x,3)
    # 0 mewakili r, 1 mewakili g, 2 mewakili b, 3 mewakili alpha
    red_im = im[:,:,0]
    green_im = im[:,:,1]
    blue_im = im[:,:,2]
    alp_im = im[ :, :,3]
    
    #mengembalikan ukuran array dan keempat rgba based array
    return red_im, green_im, blue_im,alp_im

