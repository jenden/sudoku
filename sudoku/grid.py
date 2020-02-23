from typing import List


class Grid:

    def __init__(self, grid: List[List]):
        self._grid = grid

        self._rows = None
        self._cols = None
        self._subgrids = None

    def __getitem__(self, index):
        try:
            x, y = index

            if y == slice(None, None, None):
                return Column([row[x - 1] for row in self._grid])
            elif x == slice(None, None, None):
                return Row(self._grid[y - 1])
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

    @property
    def rows(self) -> 'RowGenerator':
        if self._rows is None:
            self._rows = RowGenerator(self)
        return self._rows

    @property
    def cols(self) -> 'ColumnGenerator':
        if self._cols is None:
            self._cols = ColumnGenerator(self)
        return self._cols

    @property
    def subgrids(self) -> 'SubgridGenerator':
        if self._subgrids is None:
            self._subgrids = SubgridGenerator(self._grid)
        return self._subgrids

    def subgrid_at(self, x, y):
        return self.subgrids.at(x, y)

    def items(self):
        for y, row in enumerate(self._grid, start=1):
            for x, value in enumerate(row, start=1):
                yield x, y, value

    def is_valid(self) -> bool:
        """True if the grid is 9 x 9 and contains only legal values"""
        pass

    def is_solved(self) -> bool:
        """True if the grid is solved"""
        complete = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        rows_complete = all(set(row) == complete for row in self.rows)
        cols_complete = all(set(col) == complete for col in self.cols)
        subgrids_complete = all(set(subgrid) == complete for subgrid in self.subgrids)

        return rows_complete and cols_complete and subgrids_complete



    def __repr__(self):
        return f'Grid({self._grid})'

    def __str__(self):
        rows = ['| {}  {}  {} | {}  {}  {} | {}  {}  {} |'.format(*row)
                for row in self._grid]
        [rows.insert(i, '+ -  -  - + -  -  - + -  -  - +') for i in [9, 6, 3, 0]]
        return '\n'.join(rows).replace('0', ' ')


class SubgridGenerator:

    def __init__(self, grid: List[List[int]]):
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

    def __str__(self):
        rows = ['| {}  {}  {} |'.format(*row) for row in self._subgrid]
        rows.append('+ -  -  - +')
        rows.insert(0, rows[-1])
        return '\n'.join(rows).replace('0', ' ')

    def __eq__(self, other):
        return self._subgrid == other._subgrid


class ColumnGenerator:

    def __init__(self, grid: Grid):
        self._grid = grid

    def __getitem__(self, x):
        try:
            return Column(self._grid[x, :])
        except (ValueError, TypeError, IndexError):
            raise IndexError(f'Unable to get column at index `{x}`')

    def __iter__(self):
        for x in range(1, 10):
            yield self._grid[x, :]


class Column(list):

    def __init__(self, column: List[int]):
        super().__init__()
        [self.append(e) for e in column]

    def __getitem__(self, y):
        return self[y-1]

    def __repr__(self):
        return '[' + ',\n '.join([str(e) for e in self]) + ']'


class RowGenerator:

    def __init__(self, grid):
        self._grid = grid

    def __getitem__(self, y):
        try:
            return Row(self._grid[:, y])
        except (ValueError, TypeError, IndexError):
            raise IndexError(f'Unable to get row at index `{y}`')

    def __iter__(self):
        for y in range(1, 10):
            yield self._grid[:, y]


class Row(list):

    def __init__(self, row: List[int]):
        super().__init__()
        [self.append(e) for e in row]

    def __getitem__(self, x):
        return self[x-1]
