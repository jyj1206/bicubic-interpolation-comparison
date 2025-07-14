from scipy.ndimage import zoom
import numpy as np
import time

def scipy_bicubic(rgb_image, scale):
    factor = 1 / scale
    
    start = time.time()
    resized = zoom(rgb_image, (factor, factor, 1), order=3)
    result = np.clip(resized, 0, 255).astype(np.uint8)
    end = time.time()
    
    return result, end - start
