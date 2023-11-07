#!/usr/bin/env python

from tango.server import Device, attribute


class SarMoto(Device):
    _position = attribute(name="Position", dtype=float)

    @_position.setter
    def _pos_set(self, value):
        print(f"set pos to {value=}")


if __name__ == "__main__":
    SarMoto.run_server()
