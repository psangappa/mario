""" This module validates the incoming data.
For example:    if the given grid is not a square matrix
                if there are more than one mario and princes
"""
from app.save_princess.const import ALLOWED_SYMBOLS, MARIO, PRINCESS, OBSTACLE


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
            valid_symbols = list(map(lambda s: s in ALLOWED_SYMBOLS, row))
            if not all(valid_symbols):
                self.message = 'Only m, p, -, x symbols are allowed'
                return False
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
        return True
