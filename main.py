import numpy as np
import os
from PIL import Image

from interpolation_method import cv2_bicubic, pil_bicubic, torch_bicubic_cpu, torch_bicubic_gpu, matlab_bicubic, quit_matlab
from metric import evaluate_psnr, evaluate_time
import matplotlib.pyplot as plt

def main():
    hr_path = 'data/HR'
    lr_path = 'data/LR'
    
    data_path = '0003.png'
    scale = 4
    
    hr_image = Image.open(os.path.join(hr_path, data_path))
    hr_image = np.array(hr_image)
    
    name, format = data_path.split('.')
    gt_image = Image.open(os.path.join(lr_path, f'{name}x{scale}.{format}'))
    gt_image = np.array(gt_image)
        
    result_dict = {}
    
    methods = [
        cv2_bicubic,
        pil_bicubic,
        torch_bicubic_cpu,
        torch_bicubic_gpu,
        matlab_bicubic
    ]
    
    try:
        for method in methods:
            result, avg_time = evaluate_time(method, hr_image, scale)
            psnr = evaluate_psnr(gt_image, result)
            is_same = np.array_equal(gt_image, result) 
            result_dict[method.__name__] = {
                'result': result,
                'avg_time': avg_time,
                'psnr': psnr,
                'same': is_same
            }

        # 시각화
        n_methods = len(result_dict)
        plt.figure(figsize=(16, 3 + 2 * n_methods))
        
        # HR 이미지
        plt.subplot(1, n_methods + 2, 1)
        plt.imshow(hr_image)
        plt.title('High Resolution (Original)', fontsize=9)
        plt.axis('off')
        
        # GT 이미지 (Downsampled)
        plt.subplot(1, n_methods + 2, 2)
        plt.imshow(gt_image)
        plt.title('Low Resolution (Ground Truth)', fontsize=9)
        plt.axis('off')
        
        # 결과 이미지 + 점수
        for i, (method, scores) in enumerate(result_dict.items(), start=3):
            plt.subplot(1, n_methods + 2, i)
            plt.imshow(scores['result'])
            plt.title(
                f"{method}\n{scores['psnr']:.1f} dB | {scores['avg_time']*1000:.1f} ms | same : {'O' if scores['same'] else 'X'}",
                fontsize=9
            )
            plt.axis('off')
        
        plt.tight_layout()
        plt.show()    
    finally:
        quit_matlab() 

if __name__ == '__main__':
    main()
