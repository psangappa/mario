""" This module validates the incoming data.
For example:    if the given grid is not a square matrix
                if there are more than one mario and princes
"""
from app.save_princess.const import *


class Validator:
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid.split(',')
        self.mario_index = []
        self.princess_index = []
        self.obstacles = []
        self.message = ''

    def validate(self):
        """
        :return: False if any of the constrains are violated. True otherwise
        """
        if self.n <= 1 or not self.grid or len(self.grid) != self.n:
            self.message = 'The given grid or grid-size n does not match'
            return False
        for index, row in enumerate(self.grid):
            if len(row) != self.n:
                self.message = 'One of the row in the grid has invalid size'
                return False
            # check if user enters invalid symbols other than m, p, x, -
            valid_symbols = list(map(lambda s: s in ALLOWED_SYMBOLS, row))
            if not all(valid_symbols):
                self.message = 'Only m, p, -, x symbols are allowed'
                return False
            # check if the entire row is filled with obstacles.
            if self.row_filled_with_obstacles(row):
                self.message = 'Obstacles Everywhere'
            if MARIO in row:
                if self.mario_index or row.count(MARIO) > 1:
                    # we found our hero second time or twice in a given row
                    self.message = 'Only one Mario allowed'
                    return False
                self.mario_index = [index, row.index(MARIO)]
            if PRINCESS in row:
                if self.princess_index or row.count(PRINCESS) > 1:
                    # we found our princess second time or twice in a given row
                    self.message = 'Only one Princes allowed'
                    return False
                self.princess_index = [index, row.index(PRINCESS)]
            if OBSTACLE in row:
                x_index = [i for i, x in enumerate(row) if x == OBSTACLE]
                for x in x_index:
                    self.obstacles.append([index, x])
        if not self.princess_index or not self.mario_index:
            # we never found our mario or princess
            self.message = 'At least one Mario or Princess is required to play the game'
            return False
        if self.message == 'Obstacles Everywhere':
            return False
        if self.surrounded_by_x(self.princess_index[0], self.princess_index[1]) or self.surrounded_by_x(
                self.mario_index[0], self.mario_index[0]):
            self.message = 'Obstacles Everywhere'
            return False
        return True

    def row_filled_with_obstacles(self, row):
        """
        check if the entire row is filled with obstacles.
        Off course this depends on the position of mario and princes.
        :param row: row
        :return: True if the entire row is filled with obstacles.
        """
        return (self.mario_index or self.princess_index) and not (
                self.mario_index and self.princess_index) and 'x' in row and len(set(row)) == 1

    def surrounded_by_x(self, i, j):
        """
        -,-,-,m     -,-,-,m     -,-,x,m
        -,-,x,-     -,-,-,-     -,-,-,x
        -,x,p,x     -,-,-,x     -,-,-,-
        -,-,x,-     -,-,x,p     -,-,-,p
        In the above cases, return True.
        :param i: row position of mario or princess
        :param j: col position of mario or princess
        :return: True if covered with obstacles
        """
        obstacles = []
        for move in [UP, DOWN, LEFT, RIGHT]:
            if move == UP:
                if i - 1 < 0 or self.grid[i - 1][j] == OBSTACLE:
                    obstacles.append(True)
            elif move == DOWN:
                if i + 1 >= self.n or self.grid[i + 1][j] == OBSTACLE:
                    obstacles.append(True)
            elif move == LEFT:
                if j - 1 < 0 or self.grid[i][j - 1] == OBSTACLE:
                    obstacles.append(True)
            elif move == RIGHT:
                if j + 1 >= self.n or self.grid[i][j + 1] == OBSTACLE:
                    obstacles.append(True)
        if len(obstacles) == 4:
            return True
        return False
