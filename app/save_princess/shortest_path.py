from itertools import permutations

from app.save_princess.const import UP, DOWN, LEFT, RIGHT


def form_shortest_paths(mario_index, princess_index):
    """
    First we will ignore the obstacles to find shortest paths
    This method follows the below rules to find the shortest path.
    If the row difference from Princess to Mario is negative then Mario has to move UP
    If the column difference from Princess to Mario is negative then Mario has to move LEFT
    :param mario_index: index of Mario
    :param princess_index: index of Princes
    :return: set of possible shortest paths
    """
    difference_in_rows = princess_index[0] - mario_index[0]
    difference_in_cols = princess_index[1] - mario_index[1]
    ups_downs = [UP] * abs(difference_in_rows) if difference_in_rows < 0 else [DOWN] * difference_in_rows
    lefts_rights = [LEFT] * abs(difference_in_cols) if difference_in_cols < 0 else [RIGHT] * difference_in_cols
    return set(permutations(ups_downs + lefts_rights))
