import cv2
import numpy as np

def roi(img):
    mask = np.zeros(img.shape, np.uint8)
    mask[950:1080, 100:1820] = 255    ## Step 0
    mask[800:1080, 250:1820] = 255  ## Step 1
    mask[700:1080, 760:1160] = 0
    mask[600:800, 460: 1540] = 255  ## Step 2   좌핸들 ==> 우측이 더 많이 나오도록 마스킹
    mask[450:600, 730:1190] = 255   ## Step 3
    mask[340:450, 850: 1070] = 255  ## Step 4
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