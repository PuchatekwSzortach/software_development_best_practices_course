"""
Module with unit tests
"""

import pytest

import utilities


def test_factorial_for_positive_inputs():
    """
    Test factorial implementation with typical input
    """

    input = 1

    expected = 1
    actual = utilities.get_factorial(input)

    assert expected == actual

    input = 2

    expected = 2
    actual = utilities.get_factorial(input)

    assert expected == actual

    input = 3

    expected = 6
    actual = utilities.get_factorial(input)

    assert expected == actual

    input = 4

    expected = 24
    actual = utilities.get_factorial(input)

    assert expected == actual


def test_factorial_with_zero_input():
    """
    Test factorial implementation with input 0
    """

    input = 0

    expected = 1
    actual = utilities.get_factorial(input)

    assert expected == actual


def test_factorial_with_negative_input():
    """
    Test factorial implementation with negative input
    """

    with pytest.raises(ValueError):

        utilities.get_factorial(-1)
