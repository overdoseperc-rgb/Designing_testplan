import pytest
from functions import is_even

@pytest.mark.parametrize("number, expected", [(0, True), (2, True), (8, True), (-4, True), (10**20, True), (1, False), (7, False), (-3, False), (10**20 + 1, False)])
def test_is_even_positive(number, expected):
    assert is_even(number) is expected

@pytest.mark.parametrize("number", [None, "2", 2.0, 2.5, True, False, [], {}, complex(2, 0)])
def test_is_even_negative(number):
    with pytest.raises(TypeError):
        is_even(number)
