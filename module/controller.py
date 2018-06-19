import pyvjoy

class Controller:
    def __init__(self):
        try:
            self.joy = pyvjoy.VJoyDevice(1)
        except pyvjoy.vJoyFailedToAcquireException:
            print("이미 가상 컨트롤러가 사용중입니다.")
            exit(1)

    def setDirection(self, angle):
        self.joy.data.wAxisX = angle
        self.joy.update()

