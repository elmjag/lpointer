from math import pi


def rad_to_deg(rad: float) -> float:
    return rad * (180.0 / pi)


def deg_to_rad(deg: float) -> float:
    return deg * (pi / 180)


def clamp(name: str, value: float, min_val: float, max_val: float) -> float:
    if value < min_val:
        print(f"WARNING: clamping {name} from {value} to min value {min_val}")
        value = min_val

    if value > max_val:
        print(f"WARNING: clamping {name} from {value} to max value {max_val}")
        value = max_val

    return value
