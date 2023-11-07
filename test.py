#!/usr/bin/env python3

import time
from puck_pos import get_puck_xy
from angles import pos2angles
from client import set_angles


def pos_angles(puck_pos):
    x, y = get_puck_xy(puck_pos)
    base, mount = pos2angles(x, y)
    print(f"{puck_pos} x {x:.3f} y {y:.3f} base {base:.3f} mount {mount:.3f}")
    return base, mount


def mark_all_pos():
    for puck_pos in range(1, 30):
        x, y = get_puck_xy(puck_pos)
        base, mount = pos2angles(x, y)

        print(f"{puck_pos} ({x},{y}) {mount=} {base=}")
        set_angles(base, mount)
        time.sleep(2)


def oscillate():
    for mount in range(-30, 31, 1):
        for base in range(0, 60, 1):
            set_angles(base, mount)
            time.sleep(0.5)


def misc_angles():
    # set_angles(45, 30)
    set_angles(-45, 30)


def misc_mount_angles():
    for pos in [13, 8, 9, 15, 19, 20]:
        _, mount = pos_angles(pos)

        print(pos, mount)

    for pos in [2, 4, 24, 26]:
        _, mount = pos_angles(pos)

        print(pos, mount)

    for pos in [1, 5, 27, 23]:
        _, mount = pos_angles(pos)

        print(pos, mount)


def misc_base_angles():
    pos = 7
    base, _ = pos_angles(pos)

    print(pos, base)


def mark_positions(positions):
    for pos in positions:
        base, mount = pos_angles(pos)
        print(pos, base, mount)
        set_angles(base, mount)
        time.sleep(0.8)


mark_positions(range(1, 30))
