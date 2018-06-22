import cv2
import numpy as np

def roi(img):
    mask = np.zeros(img.shape, np.uint8)
    mask[800:1080, 300:1620] = 255
    mask[600:800, 450: 1370] = 255
    mask[450:600, 730:1190] = 255
    mask[340:450, 850: 1070] = 255
    # cv2.imshow("img", img)
    # cv2.imshow("mask", mask)
    # cv2.waitKey()
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    res = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("result", res)
    return res

def morp(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    res1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    res2 = cv2.morphologyEx(res1, cv2.MORPH_OPEN, kernel2)


    return res1