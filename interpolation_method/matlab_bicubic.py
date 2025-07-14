import matlab.engine
import numpy as np
import time
import os

eng = matlab.engine.start_matlab()

this_dir = os.path.dirname(os.path.abspath(__file__))
matlab_func_path = os.path.join(this_dir)
eng.addpath(matlab_func_path)

def matlab_bicubic(rgb_image, scale):    
    factor = 1 / scale
    
    # NumPy → MATLAB 형식 변환 (H x W x 3 → list → uint8)
    if rgb_image.dtype != np.uint8:
        rgb_image = (rgb_image * 255).astype(np.uint8)

    r = matlab.uint8(rgb_image[:, :, 0].tolist())
    g = matlab.uint8(rgb_image[:, :, 1].tolist())
    b = matlab.uint8(rgb_image[:, :, 2].tolist())
    matlab_img = eng.cat(3, r, g, b)
    
    # MATLAB 함수 실행
    result, elapsed = eng.matlab_bicubic(matlab_img, float(factor), nargout=2)
    
    return result, elapsed


def quit_matlab():
    eng.quit()