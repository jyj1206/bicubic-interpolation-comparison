import numpy as np
def evaluate_psnr(img1, img2, MAX_PIXEL=255.0):
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    psnr = 10 * np.log10((MAX_PIXEL)**2 / mse)
    return psnr