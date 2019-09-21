""" This module has the logic of finding princess
    Let's consider the below example
    n = 3
    grid =  --m
            -x-
            -p-
    Things to note: The shortest path to princes can be found by having these combination in the path (UP, LEFT)
                    (UP, RIGHT) (DOWN, LEFT) (DOWN, RIGHT).
                    For example, you cannot have a shortest path which includes UP and DOWN or LEFT and RIGHT.
    If the row difference from Princess to Mario is negative then Mario has to move UP
    If the column difference from Princess to Mario is negative then Mario has to move LEFT
"""
from itertools import permutations

from app.save_princess.validator import Validator
from app.save_princess.possible_path import PossiblePathFinder
from app.save_princess.const import UP, DOWN, RIGHT, LEFT, MOVES_DICT


def save_princess(n, grid, game_mode=False):
    """
    Things to note: If you're moving DOWN or UP then you add/subtract row index. Otherwise add/subtract column index
    :param n: grid size
    :param grid: a string containing rows separated by commas - '--m,-x-,-p-'
    :param game_mode: True if the request is coming from the dashboard
    :return: Error_Code, Path.
             True, [] - if any of the constrains are violated. Here True is the
             False, [] - if all paths to princess are blocked by obstacles
             False, [Path] - if we find a shortest path or a possible path to princess
    """
    validated = Validator(n, grid)
    if not validated.validate():
        return (True, [], validated) if game_mode else (True, [])
    for moves in form_shortest_paths(validated.mario_index, validated.princess_index):
        number_of_moves = len(moves)
        current_vertex = validated.mario_index.copy()
        count = 0
        for move in moves:
            if DOWN in move or UP in move:
                current_vertex[0] += MOVES_DICT[move]
            else:
                current_vertex[1] += MOVES_DICT[move]
            if current_vertex in validated.obstacles:
                # found obstacle so skip the remaining moves
                continue
            count += 1
        if count == number_of_moves:
            return (False, list(moves), validated) if game_mode else (False, list(moves))
    visited = []
    for i in range(n):
        visited.append([0]*n)
    path_finder = PossiblePathFinder()
    path_finder.find_possible_path(validated.mario_index[0], validated.mario_index[1], n, validated.grid, visited, [])
    return (False, path_finder.possible_path, validated) if game_mode else (False, path_finder.possible_path)


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
