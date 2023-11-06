from math import sqrt
from dataclasses import dataclass

PUCK_DIAMETER = 1.0

ROW_Y_OFFSET = sqrt(PUCK_DIAMETER**2 - (PUCK_DIAMETER / 2) ** 2)


@dataclass
class PuckRow:
    first_puck: int
    last_puck: int


ROWS = [
    PuckRow(1, 5),
    PuckRow(6, 11),
    PuckRow(12, 16),
    PuckRow(17, 22),
    PuckRow(23, 27),
    PuckRow(28, 29),
]


def _get_puck_grid_coord(puck_pos):
    for row, i in zip(ROWS, range(1, len(ROWS) + 1)):
        if row.first_puck <= puck_pos <= row.last_puck:
            return i, puck_pos - row.first_puck + 1

    assert False, f"unexpected puck position {puck_pos}"


def _get_row_x_offset(row_num):
    if row_num % 2 == 0:
        if row_num == 6:
            # special case for row 6 with only two pucks
            return -0.5 * PUCK_DIAMETER

        # even row number
        return -2.5 * PUCK_DIAMETER

    # normal odd row number
    return -2.0 * PUCK_DIAMETER


def get_puck_xy(puck_pos):
    row, row_pos = _get_puck_grid_coord(puck_pos)
    x = _get_row_x_offset(row) + (row_pos - 1) * PUCK_DIAMETER
    y = (3 - row) * ROW_Y_OFFSET

    return x, y


#
# for puck_pos in range(1, 30):
#     x, y = get_puck_xy(puck_pos)
#     print(f"{puck_pos} {x} {y}")
