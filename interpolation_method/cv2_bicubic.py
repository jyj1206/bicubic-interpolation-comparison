import cv2
import time

def cv2_bicubic(rgb_image, scale):

    bgr_image = rgb_image[:, :, ::-1]  # RGB → BGR
    h, w = bgr_image.shape[:2]

    start = time.time()

    resized = cv2.resize(
        bgr_image, (w // scale, h // scale), interpolation=cv2.INTER_CUBIC
    )

    result = resized[:, :, ::-1]  # BGR → RGB
    end = time.time()

    return result, end - start