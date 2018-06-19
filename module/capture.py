import pyautogui
import numpy as np

class Capture:
    def __init__(self):
        pass

    def export(self):
        image = pyautogui.screenshot()
        return np.array(image)