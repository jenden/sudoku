from typing import List


class Grid:

    def __init__(self, grid: List[List]):
        self._grid = grid

    def __getitem__(self, index):
        try:
            x, y = index

            if y == slice(None, None, None):
                return [row[x - 1] for row in self._grid]
            elif x == slice(None, None, None):
                # y is a slice, take the whole x column
                return self._grid[y - 1]
            elif isinstance(x, int) and isinstance(y, int):
                return self._grid[y - 1][x - 1]
            else:
                raise ValueError()
        except (ValueError, TypeError, IndexError):
            raise IndexError(f'Unable to get item at index `{index}`')

    def __setitem__(self, index, value):
        try:
            x, y = index
            self._grid[y - 1][x - 1] = value
        except (TypeError, ValueError, IndexError):
            raise IndexError(f'Unable to set item at index `{index}`')
    
    def subgrid(self, x, y):
        x0 = (x - 1) * 3
        y0 = (y - 1) * 3

        return [row[x0:x0+3] for row in self._grid[y0:y0 + 3]]

    def __str__(self):
        rows = [' {}  {}  {} | {}  {}  {} | {}  {}  {} '.format(*row) for row in self._grid]
        [rows.insert(i, ' -  -  - + -  -  - + -  -  - ') for i in [6, 3]]
        return '\n'.join(rows).replace('0', ' ')
