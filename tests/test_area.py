import pytest
from functions import calculate_area

@pytest.mark.parametrize("length, width, expected", [(2, 3, 6), (3, 2, 6), (5, 5, 25), (0, 8, 0), (8, 0, 0), (0, 0, 0), (2.5, 4, 10), (0.1, 0.2, 0.02), (1000, 2000, 2000000)])
def test_area_cases(length, width, expected):
    assert calculate_area(length, width) == pytest.approx(expected)

@pytest.mark.parametrize("length", [0, 2, 2.5])
@pytest.mark.parametrize("width", [0, 3, 0.2])
def test_area_combinations(length, width):
    expected = {(0, 0): 0, (0, 3): 0, (0, 0.2): 0, (2, 0): 0, (2, 3): 6, (2, 0.2): 0.4, (2.5, 0): 0, (2.5, 3): 7.5, (2.5, 0.2): 0.5}
    assert calculate_area(length, width) == pytest.approx(expected[length, width])

@pytest.mark.parametrize("length, width, error", [(-1, 3, ValueError), (3, -1, ValueError), (float("nan"), 1, ValueError), (1, float("inf"), ValueError), ("2", 3, TypeError), (3, None, TypeError), (True, 2, TypeError), (2, [], TypeError)])
def test_area_negative(length, width, error):
    with pytest.raises(error):
        calculate_area(length, width)
