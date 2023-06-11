import os
import tifffile

def tile(filename, dir_in, dir_out):
    name, ext = os.path.splitext(filename)
    img = tifffile.imread(os.path.join(dir_in, filename))

    windowsize_r = 1000
    windowsize_c = 1000

    i = 0
    for r in range(0, img.shape[0] - windowsize_r, windowsize_r):
        for c in range(0, img.shape[1] - windowsize_c, windowsize_c):
            window = img[r:r + windowsize_r, c:c + windowsize_c]
            out = os.path.join(dir_out, f'{name}_{i}_{ext}')
            os.makedirs(dir_out, exist_ok=True)
            tifffile.imwrite(out, window)
            i = i + 1

tile('103001007A0D3500.tif','/home/aditya/Downloads/tiffs','/home/aditya/Downloads/tiffs/split')