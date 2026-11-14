"""Part C tests. Your code goes in Lab8/address.py."""
from address import address


def test_first_entry_is_at_x():
    assert address(100, 5, 1, 1) == 100


def test_moving_right_one_column_adds_1():
    assert address(100, 5, 1, 2) == 101


def test_moving_down_one_row_adds_the_number_of_columns():
    assert address(100, 5, 2, 1) == 105


def test_row_3_column_4_with_5_columns():
    assert address(100, 5, 3, 4) == 113


def test_a_wider_table():
    assert address(0, 6, 3, 4) == 15
