""" If there is no shortest path exist, then find the possible path to the princes """
from app.save_princess.const import PRINCESS, MARIO, OBSTACLE, UP, DOWN, RIGHT, LEFT


class PossiblePathFinder:
    def __init__(self, n, grid):
        self.possible_path = []
        self.n = n
        self.grid = grid

    def find_possible_path(self, i, j, visited, path, move=None):
        """
        This is a DFS with backtracking.
        This recursive method will travel through the matrix to form the possible path.
        :param i: row index of Mario
        :param j: column index of Mario
        :param visited: n*n list with all 0's.
        :param path: empty path
        :param move: RIGHT, LEFT, UP, DOWN
        """

        if self.possible_path:
            return
        visited[i][j] = 1
        if self.grid[i][j] == PRINCESS or self.grid[i][j] != MARIO:
            path.append(move)
        if self.grid[i][j] == PRINCESS:
            self.possible_path = path.copy()
            return

        # Up
        if i >= 1 and not visited[i - 1][j] and self.grid[i - 1][j] != OBSTACLE:
            self.find_possible_path(i - 1, j, visited, path, UP)

        # Down
        if i < self.n - 1 and not visited[i + 1][j] and self.grid[i + 1][j] != OBSTACLE:
            self.find_possible_path(i + 1, j, visited, path, DOWN)

        # Left
        if j >= 1 and not visited[i][j - 1] and self.grid[i][j - 1] != OBSTACLE:
            self.find_possible_path(i, j - 1, visited, path, LEFT)

        # Right
        if j < self.n - 1 and not visited[i][j + 1] and self.grid[i][j + 1] != OBSTACLE:
            self.find_possible_path(i, j + 1, visited, path, RIGHT)

        visited[i][j] = 0
        if path:
            path.pop()
