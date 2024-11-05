from multiplier import multiply_two_numbers
import pytest

def test_multiply_positive_numbers():
    assert multiply_two_numbers(3.5, 2.0) == pytest.approx(7.0)

def test_multiply_negative_numbers():
    assert multiply_two_numbers(-2.0, -3.0) == pytest.approx(6.0)

def test_multiply_by_zero():
    assert multiply_two_numbers(0, 100) == pytest.approx(0)
    assert multiply_two_numbers(100, 0) == pytest.approx(0)

def test_multiply_mixed_sign_numbers():
    assert multiply_two_numbers(-3.0, 3.0) == pytest.approx(-9.0)
    assert multiply_two_numbers(3.0, -4.0) == pytest.approx(-12.0)

def test_multiply_large_numbers():
    assert multiply_two_numbers(1e10, 2.0) == pytest.approx(2e10)
