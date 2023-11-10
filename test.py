#!/usr/bin/env python3

import time
from puck_pos import get_puck_xy
from angles import pos2angles
from tango_client import TangoClient
from local_client import LocalClient
from util import clamp


def pos_angles(puck_pos):
    x, y = get_puck_xy(puck_pos)
    base, mount = pos2angles(x, y)
    assert -90 <= base <= 90, "bad base"

    base = -base
    mount = -mount

    base = clamp("base", base, -87.0, 90.0)
    mount = clamp("mount", mount, -7.8, 8.0)

    print(f"{puck_pos} x {x:.3f} y {y:.3f} base {base:.3f} mount {mount:.3f}")
    return base, mount


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


def mark_positions(client, positions):
    for pos in positions:
        base, mount = pos_angles(pos)
        client.set_angles(base, mount)
        time.sleep(0.8)


# client = TangoClient()
client = LocalClient()
mark_positions(client, range(1, 30))
