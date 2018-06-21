import cv2
import numpy as np

def roi(img):
    mask = np.zeros(img.shape, np.uint8)
    mask[700:1080, 0:1920] = 255
    mask[550:800, 530:1390] = 255
    mask[440:650, 750: 1170] = 255
    # cv2.imshow("img", img)
    # cv2.imshow("mask", mask)
    # cv2.waitKey()
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    res = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("result", res)
    return res