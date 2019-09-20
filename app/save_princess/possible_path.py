""" If there is no shortest path exist, then find the possible path to the princes """


class PossiblePathFinder:
    def __init__(self):
        self.possible_path = []

    def find_possible_path(self, i, j, n, grid, visited, path, move=None):
        """
        This is a DFS with backtracking.
        This recursive method will travel through the matrix to form the possible path.
        :param i: row index of Mario
        :param j: column index of Mario
        :param n: Grid size
        :param grid: The Grid
        :param visited: n*n list with all 0's.
        :param path: empty path
        :param move: RIGHT, LEFT, UP, DOWN
        """

        if self.possible_path:
            return
        visited[i][j] = 1
        if grid[i][j] == 'p' or grid[i][j] != 'm':
            path.append(move)
        if grid[i][j] == 'p':
            self.possible_path = path.copy()
            return

        # Up
        if i >= 1 and not visited[i - 1][j] and grid[i - 1][j] != 'x':
            self.find_possible_path(i - 1, j, n, grid, visited, path, 'UP')

        # Down
        if i < n - 1 and not visited[i + 1][j] and grid[i + 1][j] != 'x':
            self.find_possible_path(i + 1, j, n, grid, visited, path, 'DOWN')

        # Left
        if j >= 1 and not visited[i][j - 1] and grid[i][j - 1] != 'x':
            self.find_possible_path(i, j - 1, n, grid, visited, path, 'LEFT')

        # Right
        if j < n - 1 and not visited[i][j + 1] and grid[i][j + 1] != 'x':
            self.find_possible_path(i, j + 1, n, grid, visited, path, 'RIGHT')

        visited[i][j] = 0
        if path:
            path.pop()
