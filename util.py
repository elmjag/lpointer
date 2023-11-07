from math import pi


def rad_to_deg(rad: float) -> float:
    return rad * (180.0 / pi)


def deg_to_rad(deg: float) -> float:
    return deg * (pi / 180)
