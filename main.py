import cv2
import time
import numpy as np

from module import controller
from module import capture
from module import imageProcess as IP

ctl = controller.Controller()
capture = capture.Capture()

whiteLow = np.array([0.09, 0, 80], np.float32)
whiteHigh = np.array([5.4, 5.25, 255], np.float32)

# ctl.setDirection(0x4000)
currentTIme = time.time()
while True:
    originImg = capture.export()
    img = IP.roi(originImg)
    # img = cv2.blur(img, (3, 3))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 # Normalize 수행
    print(np.mean(gray[800:830, :]))
    meanMask = np.full(gray.shape, 70-np.mean(gray[800:830, :]))    # np.mean의 결과: double 형

    gray = np.add(gray, meanMask)
    print(np.mean(gray[800:830, :]))

    whiteFilterRes = cv2.inRange(gray, 180, 255)

    # whiteFilterRes = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # whiteFilterRes = cv2.inRange(whiteFilterRes, whiteLow, whiteHigh)

    gray = cv2.bitwise_and(whiteFilterRes, np.array(gray, np.uint8))

    edges = cv2.Canny(gray, 50, 150)
    # edges = IP.morp(edges)

    angle = np.pi / 180
    lines = cv2.HoughLines(edges, 13, angle * 4, 1200)

    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    overSpeedMarker = originImg[730, 1500, 2]
    # print(overSpeedMarker)
    if overSpeedMarker > 80:
        cv2.putText(edges, "Warning: OverSpeed!!", (10, 40), 1, 1.2, (0, 0, 255))

    if lines is None:
        pass
    else:
        for i in range(len(lines)):
            for rho, theta in lines[i]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 2000 * (-b))
                y1 = int(y0 + 2000 * (a))
                x2 = int(x0 - 2000 * (-b))
                y2 = int(y0 - 2000 * (a))

                # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.line(edges, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.putText(edges, "Frame took {} seconds".format(time.time() - currentTIme), (10, 20), 1, 1.2, (255, 255, 255))
    currentTIme = time.time()
    # cv2.imshow("filtered", gray)
    cv2.imshow("edges", edges)
    # cv2.imshow("lines", img)
    cv2.waitKey(1)