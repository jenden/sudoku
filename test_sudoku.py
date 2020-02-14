import pytest

from sudoku import Grid


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
