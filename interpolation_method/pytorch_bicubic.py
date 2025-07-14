import torch
import torch.nn.functional as F
import numpy as np
import time

def torch_bicubic_cpu(rgb_image, scale):
    factor = 1/scale
    
    img_tensor = (
        torch.from_numpy(rgb_image)
        .permute(2, 0, 1)
        .unsqueeze(0)
        .float() / 255.0
    )

    start = time.time()
    downsampled = F.interpolate(img_tensor, scale_factor=factor, mode='bicubic', align_corners=False)
    

    result = (
        downsampled.squeeze(0)
        .permute(1, 2, 0)
        .numpy() * 255.0
    ).clip(0, 255).astype(np.uint8)
    
    end = time.time()
    return result, end - start

def torch_bicubic_gpu(rgb_image, scale):
    factor = 1/scale
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    img_tensor = (
        torch.from_numpy(rgb_image)
        .permute(2, 0, 1)
        .unsqueeze(0)
        .float()
        .to(device) / 255.0
    )

    torch.cuda.synchronize()
    start = time.time()

    downsampled = F.interpolate(img_tensor, scale_factor=factor, mode='bicubic', align_corners=False)

    result = (
        downsampled.squeeze(0)
        .permute(1, 2, 0)
        .cpu()
        .numpy() * 255.0
    ).clip(0, 255).astype(np.uint8)

    torch.cuda.synchronize()
    end = time.time()

    elapsed_time = end - start
    return result, elapsed_time