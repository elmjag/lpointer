import time
from tango import DeviceProxy



def _while_moving(*devs):
   while True:
     is_moving = [dev.StatusMoving for dev in devs]
     print(is_moving)
     if not any(is_moving):
       print("the all stopped!")
       return

     time.sleep(0.2)


class TangoClient:
    def __init__(self):
        self.azi = DeviceProxy("b311a-e/dia/alas-01-azi")
        self.pol = DeviceProxy("b311a-e/dia/alas-01-pol")

        print(self.azi.ping())
        print(self.pol.ping())

    def set_angles(self, base, mount):
        _while_moving(self.azi, self.pol)
        self.azi.Position = base
        self.pol.Position = mount
