from PIL import Image
import numpy as np
import time

def pil_bicubic(rgb_image, scale):
    img = Image.fromarray(rgb_image, mode='RGB')
    w, h = img.size

    start = time.time()
    resized = img.resize((w // scale, h // scale), resample=Image.BICUBIC)
    result = np.array(resized)
    end = time.time()

    return result, end - start
