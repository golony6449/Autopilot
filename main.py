import cv2

from module import controller
from module import capture

ctl = controller.Controller()
capture = capture.Capture()

# ctl.setDirection(0x4000)

while True:
    cv2.imshow("screenshot", capture.export())
    cv2.waitKey(1)