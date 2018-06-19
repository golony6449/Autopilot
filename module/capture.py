import pyautogui
import numpy as np
import cv2

class Capture:
    def __init__(self):
        pass

    def export(self):
        image = pyautogui.screenshot()
        output = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        return output