import pytest
from functions import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [(3, 3, 3, "равносторонний"), (0.5, 0.5, 0.5, "равносторонний"), (3, 3, 4, "равнобедренный"), (3, 4, 3, "равнобедренный"), (4, 3, 3, "равнобедренный"), (2.5, 2.5, 4, "равнобедренный"), (3, 4, 5, "разносторонний"), (5, 3, 4, "разносторонний"), (4, 5, 3, "разносторонний"), (2.5, 3.5, 4.5, "разносторонний")])
def test_triangle_types(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected

@pytest.mark.parametrize("a, b, c, error", [(1, 2, 3, ValueError), (3, 1, 2, ValueError), (1, 2, 4, ValueError), (0, 2, 2, ValueError), (2, -1, 2, ValueError), (2, 2, float("inf"), ValueError), (float("nan"), 2, 2, ValueError), ("3", 3, 3, TypeError), (3, None, 3, TypeError), (3, 3, True, TypeError)])
def test_triangle_negative(a, b, c, error):
    with pytest.raises(error):
        classify_triangle(a, b, c)
