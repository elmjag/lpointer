from math import atan, sqrt, pi, isclose
from util import deg_to_rad, rad_to_deg
from params import HEIGHT, BASE_ROTATION_OFFSET



def _get_base_rotation(x, y):
    if isclose(x, 0.0):
        # handle special cases where we need to point along the X axis

        if isclose(y, 0.0):
            # we need to point straight down
            return 0

        if y > 0:
            # we need to point 'north' of the axis origin
            return pi / 2
        else:
            # we need to point 'south' of the axis origin
            return -pi / 2

    ang = atan(abs(y) / abs(x))

    if x < 0.0:
        if y < 0.0:
            # -x -y
            ang = pi + ang
        else:
            # -x +y
            ang = pi - ang
    else:
        if y < 0.0:
            # +x -y
            ang = 2 * pi - ang
        else:
            # +x +y
            pass

    return ang


def _get_mount_rotation(x, y):
    dist = sqrt(x * x + y * y)
    ang = atan(dist / HEIGHT)

    return ang


def pos2angles(x: float, y: float) -> tuple[float, float]:
    base = rad_to_deg(_get_base_rotation(x, y)) + BASE_ROTATION_OFFSET
    mount = rad_to_deg(_get_mount_rotation(x, y))

    # the lazer pointer's rotation range is approximately -90 deg to +90 deg
    #
    # the base angle we calculate is between 0 and 360 degrees,
    # convert that angle to supported range, flipping mount angle if needed
    if base >= 90.0:
        if base >= 270.0:
            base = -(360 - base)
        else:
            base = base - 180
            mount = -mount

    return base, mount
