from adder import add_two_numbers
import pytest

def test_add_positive_numbers():
    assert add_two_numbers(3.5, 2.5) == pytest.approx(6.0)

def test_add_negative_numbers():
    assert add_two_numbers(-1.1, -2.2) == pytest.approx(-3.3)

def test_add_zero():
    assert add_two_numbers(0, 0) == pytest.approx(0)

def test_add_mixed_sign_numbers():
    assert add_two_numbers(-3.5, 3.5) == pytest.approx(0)
    assert add_two_numbers(-3.5, 7.5) == pytest.approx(4.0)

def test_add_large_numbers():
    assert add_two_numbers(1e10, 1e10) == pytest.approx(2e10)
