![Build Status](https://github.com/jenden/sudoku/workflows/Unit%20Test/badge.svg)

# sudoku
> Inspired by a [youtube video](https://www.youtube.com/watch?v=G_UYXzGuqvM).


A Grid contains a 9 x 9 matrix created as a list of lists.

```python
>>> from sudoku import Grid
>>> grid = Grid([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ])
```

Grids print in a slightly more useful representation.
```python
>>> print(grid)
+ -  -  - + -  -  - + -  -  - +
| 5  3    |    7    |         |
| 6       | 1  9  5 |         |
|    9  8 |         |    6    |
+ -  -  - + -  -  - + -  -  - +
| 8       |    6    |       3 |
| 4       | 8     3 |       1 |
| 7       |    2    |       6 |
+ -  -  - + -  -  - + -  -  - +
|    6    |         | 2  8    |
|         | 4  1  9 |       5 |
|         |    8    |    7  9 |
+ -  -  - + -  -  - + -  -  - +
```

Grids can be used with tuple indices and slices. They are 1-indexed from the top left.
```python
>>> grid[1, 1]
5
>>> grid[9, 5]
1
>>> grid[1, :]  # first column
[5, 6, 0, 8, 4, 3, 0, 0, 0]
>>> grid[:, 9]  # last row
[0, 0, 0, 0, 8, 0, 0, 7, 9]
```

When solving, it's useful to check one of the nine subgrids. You can access a grid by referencing which 3 x 3 subgrid or by accessing the subgrid that contains a specific value.
```python
>>> grid.subgrids[3, 3]
Subgrid([[0, 6, 0], [8, 0, 3], [0, 2, 0]])
>>> print(grid.subgrid_at(9, 9))
+ -  -  - +
| 5  3    |
| 6       |
|    9  8 |
+ -  -  - +
```
