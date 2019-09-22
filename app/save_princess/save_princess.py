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
from app.save_princess.shortest_path import form_shortest_paths
from app.save_princess.validator import Validator
from app.save_princess.possible_path import PossiblePathFinder
from app.save_princess.const import UP, DOWN, MOVES_DICT


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
        if validated.message == 'Obstacles Everywhere':
            return (False, [], validated) if game_mode else (False, [])
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
        visited.append([0] * n)
    path_finder = PossiblePathFinder(n, validated.grid)
    path_finder.find_possible_path(validated.mario_index[0], validated.mario_index[1], visited, [])
    return (False, path_finder.possible_path, validated) if game_mode else (False, path_finder.possible_path)
