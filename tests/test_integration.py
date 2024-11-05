from adder import add_two_numbers
from multiplier import multiply_two_numbers
import pytest

def test_add_and_multiply():
    """Test if the combined behavior of add and multiply works as expected."""
    # Example: (2 + 3) * 5 = 25
    result_add = add_two_numbers(2, 3)
    result_mult = multiply_two_numbers(result_add, 5)
    assert result_mult == pytest.approx(25.0)

def test_multiply_and_add():
    """Test if the behavior of multiply and then add works as expected."""
    # Example: 2 * 3 + 4 = 10
    result_mult = multiply_two_numbers(2, 3)
    result_add = add_two_numbers(result_mult, 4)
    assert result_add == pytest.approx(10.0)

def test_nested_operations():
    """Test combining both functions in a more complex operation."""
    # Example: (2 + 3) * (4 + 5) = 45
    result_add1 = add_two_numbers(2, 3)
    result_add2 = add_two_numbers(4, 5)
    result_mult = multiply_two_numbers(result_add1, result_add2)
    assert result_mult == pytest.approx(45.0)

def test_edge_cases():
    """Test some edge cases with zero and negative numbers."""
    # Example: (0 + 5) * (-3) = -15
    result_add = add_two_numbers(0, 5)
    result_mult = multiply_two_numbers(result_add, -3)
    assert result_mult == pytest.approx(-15.0)
