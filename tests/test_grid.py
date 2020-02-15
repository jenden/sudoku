import pytest

from sudoku.grid import Grid


@pytest.fixture
def valid_grid():
    return Grid([
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


def test_instantiate_valid_grid(valid_grid):
    assert isinstance(valid_grid, Grid)


def test_get_xy(valid_grid):

    assert valid_grid[1, 1] == 5
    assert valid_grid[9, 4] == 3
    assert valid_grid[9, 9] == 9


def test_get_x_slice(valid_grid):
    expected = [5, 6, 0, 8, 4, 7, 0, 0, 0]
    actual = valid_grid[1, :]

    assert actual == expected


def test_get_y_slice(valid_grid):
    expected = [7, 0, 0, 0, 2, 0, 0, 0, 6]
    actual = valid_grid[:, 6]
    assert actual == expected


def test_get_bad_slices(valid_grid):

    with pytest.raises(IndexError):
        valid_grid[1, 2, 3]

    with pytest.raises(IndexError):
        valid_grid[1::2]

    with pytest.raises(IndexError):
        valid_grid[1]

    with pytest.raises(IndexError):
        valid_grid[0, 10]


def test_set_xy(valid_grid):

    valid_grid[1, 1] = 9
    assert valid_grid[1, 1] == 9


def test_set_bad_slice(valid_grid):

    with pytest.raises(IndexError):
        valid_grid[1] = 0

    with pytest.raises(IndexError):
        valid_grid[1::2] = 0 

    with pytest.raises(IndexError):
        valid_grid[10, 10] = 0

    with pytest.raises(IndexError):
        valid_grid[1, 2, 3] = 0


def test_get_subgrid(valid_grid):
    expected = [
        [0, 0, 0],
        [4, 1, 9],
        [0, 8, 0],
    ]

    actual = valid_grid.subgrid(2, 3)
    assert actual == expected


def test_str(valid_grid):
    expected = ' 5  3    |    7    |         \n' + \
               ' 6       | 1  9  5 |         \n' + \
               '    9  8 |         |    6    \n' + \
               ' -  -  - + -  -  - + -  -  - \n' + \
               ' 8       |    6    |       3 \n' + \
               ' 4       | 8     3 |       1 \n' + \
               ' 7       |    2    |       6 \n' + \
               ' -  -  - + -  -  - + -  -  - \n' + \
               '    6    |         | 2  8    \n' + \
               '         | 4  1  9 |       5 \n' + \
               '         |    8    |    7  9 '
    actual = str(valid_grid)
    assert actual == expected
