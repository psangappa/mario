""" This module validates the incoming data.
For example:    if the given grid is not a square matrix
                if there are more than one mario and princes
"""


class Validator:
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid.split(',')
        self.mario_index = []
        self.princess_index = []
        self.obstacles = []

    def validate(self):
        """
        :return: False if any of the constrains are violated. True otherwise
        """
        if self.n <= 1 or not self.grid or len(self.grid) != self.n:
            return False
        for index, row in enumerate(self.grid):
            if len(row) != self.n:
                return False
            if 'm' in row:
                if self.mario_index or row.count('m') > 1:
                    # we found our hero second time or twice in a given row
                    return False
                self.mario_index = [index, row.index('m')]
            if 'p' in row:
                if self.princess_index or row.count('p') > 1:
                    # we found our princess second time or twice in a given row
                    return False
                self.princess_index = [index, row.index('p')]
            if 'x' in row:
                x_index = [i for i, x in enumerate(row) if x == 'x']
                for x in x_index:
                    self.obstacles.append([index, x])
        if not self.princess_index or not self.mario_index:
            # we never found our mario or princess
            return False
        return True
