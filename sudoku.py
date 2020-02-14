from typing import List


class Grid:

    def __init__(self, grid):
        self._grid = grid

    def __getitem__(self, value):
        try:
            x, y = value

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
            raise IndexError(f'Unable to index {value}')
