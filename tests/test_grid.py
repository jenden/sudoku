import pytest

from sudoku.grid import Grid, Subgrid, Column


@pytest.fixture
def valid_grid() -> Grid:
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


@pytest.fixture
def solved_grid() -> Grid:
    return Grid([
        [2, 4, 9, 6, 5, 8, 3, 7, 1],
        [1, 3, 6, 2, 7, 9, 5, 8, 4],
        [7, 5, 8, 3, 1, 4, 2, 9, 6],
        [4, 8, 7, 9, 3, 5, 6, 1, 2],
        [3, 9, 2, 1, 6, 7, 4, 5, 8],
        [5, 6, 1, 4, 8, 2, 7, 3, 9],
        [9, 1, 3, 7, 4, 6, 8, 2, 5],
        [6, 2, 5, 8, 9, 3, 1, 4, 7],
        [8, 7, 4, 5, 2, 1, 9, 6, 3],
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


def test_column_str(valid_grid):
    expected = '[5,\n' \
               ' 6,\n' \
               ' 0,\n' \
               ' 8,\n' \
               ' 4,\n' \
               ' 7,\n' \
               ' 0,\n' \
               ' 0,\n' \
               ' 0]'

    column = valid_grid[1, :]

    assert isinstance(column, Column)
    assert str(column) == expected


def test_get_y_slice(valid_grid):
    expected = [7, 0, 0, 0, 2, 0, 0, 0, 6]
    actual = valid_grid[:, 6]
    assert actual == expected


def test_get_bad_indices(valid_grid):

    with pytest.raises(IndexError):
        _ = valid_grid[1, 2, 3]

    with pytest.raises(IndexError):
        _ = valid_grid[1::2]

    with pytest.raises(IndexError):
        _ = valid_grid[1]

    with pytest.raises(IndexError):
        _ = valid_grid[0, 10]

    with pytest.raises(IndexError):
        _ = valid_grid[1, 'b']


def test_set_xy(valid_grid):

    valid_grid[1, 1] = 9
    assert valid_grid[1, 1] == 9


def test_set_bad_indices(valid_grid):

    with pytest.raises(IndexError):
        valid_grid[1] = 0

    with pytest.raises(IndexError):
        valid_grid[1::2] = 0

    with pytest.raises(IndexError):
        valid_grid[10, 10] = 0

    with pytest.raises(IndexError):
        valid_grid[1, 2, 3] = 0


def test_get_subgrid(valid_grid):
    expected = Subgrid([
        [0, 0, 0],
        [4, 1, 9],
        [0, 8, 0],
    ])

    actual = valid_grid.subgrids[2, 3]
    assert actual == expected


def test_get_subgrid_at(valid_grid):
    expected = Subgrid([
        [0, 0, 3],
        [0, 0, 1],
        [0, 0, 6],
    ])

    for x, y in [(7, 4), (9, 6), (7, 5)]:
        assert valid_grid.subgrid_at(x, y) == expected


def test_get_subgrid_bad_indices(valid_grid):

    with pytest.raises(IndexError):
        valid_grid.subgrids[1]

    with pytest.raises(IndexError):
        valid_grid.subgrids[1::2]

    with pytest.raises(IndexError):
        valid_grid.subgrids[1, 2, 3]


def test_subgrid_iter():
    subgrid = Subgrid([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3],
    ])

    expected = {0, 1, 2, 3}
    actual = set(subgrid)

    assert actual == expected


def test_subgrid_generator_iter(valid_grid):
    expected_subgrids = 9

    actual_subgrids = 0
    for subgrid in valid_grid.subgrids:
        actual_subgrids += 1

    assert actual_subgrids == expected_subgrids


def test_subgrid_str(valid_grid):
    expected = '+ -  -  - +\n' + \
               '|    6    |\n' + \
               '| 8     3 |\n' + \
               '|    2    |\n' + \
               '+ -  -  - +'

    actual = str(valid_grid.subgrids[2, 2])
    assert actual == expected


def test_subgrid_repr(valid_grid):
    expected = 'Subgrid([[5, 3, 0], [6, 0, 0], [0, 9, 8]])'

    subgrid = valid_grid.subgrids[1, 1]
    assert repr(subgrid) == expected


def test_iterate_over_grid(valid_grid):
    expected_items = 81

    actual_items = 0
    for x, y, value in valid_grid.items():
        assert value == valid_grid[x, y]
        actual_items += 1

    assert actual_items == expected_items


def test_row_generator_getitem(valid_grid):
    expected = [0, 0, 0, 0, 8, 0, 0, 7, 9]

    actual = valid_grid.rows[9]

    assert actual == expected


def test_iterate_over_rows(valid_grid):
    count = 0
    for row in valid_grid.rows:
        assert len(row) == 9
        count += 1
    assert count == 9


def test_column_generator_getitem(valid_grid):
    expected = [0, 0, 0, 3, 1, 6, 0, 5, 9]

    actual = valid_grid.cols[9]

    assert actual == expected


def test_iterate_over_cols(valid_grid):
    count = 0
    for col in valid_grid.cols:
        assert len(col) == 9
        count += 1
    assert count == 9


def test_grid_str(valid_grid):
    expected = '+ -  -  - + -  -  - + -  -  - +\n' + \
               '| 5  3    |    7    |         |\n' + \
               '| 6       | 1  9  5 |         |\n' + \
               '|    9  8 |         |    6    |\n' + \
               '+ -  -  - + -  -  - + -  -  - +\n' + \
               '| 8       |    6    |       3 |\n' + \
               '| 4       | 8     3 |       1 |\n' + \
               '| 7       |    2    |       6 |\n' + \
               '+ -  -  - + -  -  - + -  -  - +\n' + \
               '|    6    |         | 2  8    |\n' + \
               '|         | 4  1  9 |       5 |\n' + \
               '|         |    8    |    7  9 |\n' + \
               '+ -  -  - + -  -  - + -  -  - +'
    actual = str(valid_grid)
    assert actual == expected


def test_grid_repr(valid_grid):
    expected = f'Grid({valid_grid._grid})'
    actual = repr(valid_grid)

    assert actual == expected


def test_grid_solved_true(solved_grid):
    assert solved_grid.is_solved()


def test_grid_solved_false(valid_grid):
    assert not valid_grid.is_solved()
