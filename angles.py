from math import atan, sqrt, pi, isclose

HEIGHT = 4.0


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

    ang = atan(y / abs(x))

    if x < 0.0:
        ang = pi - ang

    return ang


def _get_mount_rotation(x, y):
    dist = sqrt(x * x + y * y)
    ang = atan(dist / HEIGHT)

    return ang


def _rad_to_deg(rad: float) -> float:
    return rad * (180.0 / pi)


def pos2angles(x: float, y: float) -> tuple[float, float]:
    base = _rad_to_deg(_get_base_rotation(x, y))
    mount = _rad_to_deg(_get_mount_rotation(x, y))

    return base, mount
