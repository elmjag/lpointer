from tango import DeviceProxy


class TangoClient:
    def __init__(self):
        self.azi = DeviceProxy("b311a-e/dia/alas-01-azi")
        self.pol = DeviceProxy("b311a-e/dia/alas-01-pol")

        print(self.azi.ping())
        print(self.pol.ping())

    def set_angles(self, base, mount):
        self.azi.Position = base
        self.pol.Position = mount
