from typing import List


class Grid:

    def __init__(self, grid: List[List]):
        self._grid = grid
        self.subgrids = SubgridGenerator(self._grid)

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

    def items(self):
        for y, row in enumerate(self._grid, start=1):
            for x, value in enumerate(row, start=1):
                yield x, y, value

    def possible(self, x, y, value):
        if value in self[x, :]:
            return False
        elif value in self[:, y]:
            return False
        elif value in self.subgrids.at(x, y):
            return False
        else:
            return True

    def __str__(self):
        rows = [' {}  {}  {} | {}  {}  {} | {}  {}  {} '.format(*row)
                for row in self._grid]
        [rows.insert(i, ' -  -  - + -  -  - + -  -  - ') for i in [6, 3]]
        return '\n'.join(rows).replace('0', ' ')


class SubgridGenerator:

    def __init__(self, grid):
        self._grid = grid

    def __getitem__(self, index):
        try:
            x, y = index
            x0 = (x - 1) * 3
            y0 = (y - 1) * 3

            return Subgrid([row[x0:x0+3] for row in self._grid[y0:y0 + 3]])
        except (ValueError, TypeError, IndexError):
            raise IndexError(f'Unable to get subgrid at index `{index}`')

    def at(self, x, y):
        xs, ys = (x - 1) // 3 + 1, (y - 1) // 3 + 1
        return self[xs, ys]

    def __iter__(self):
        for x in range(1, 4):
            for y in range(1, 4):
                yield self[x, y]


class Subgrid:

    def __init__(self, subgrid):
        self._subgrid = subgrid

    def __iter__(self):
        for row in self._subgrid:
            for value in row:
                yield value

    def __repr__(self):
        return f'Subgrid({self._subgrid})'

    def __eq__(self, other):
        return self._subgrid == other._subgrid
