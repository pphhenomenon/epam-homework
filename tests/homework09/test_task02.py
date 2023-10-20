import pytest

from homework09.task02 import Suppressor, suppressor


def test_class_suppressor():
    with Suppressor(IndexError):
        assert [0][1]


def test_class_suppressor_wrong_exception():
    with pytest.raises(IndexError):
        with Suppressor(ZeroDivisionError):
            [0][1]


def test_generator_suppressor():
    with suppressor(IndexError):
        assert [0][1]


def test_generator_suppressor_wrong_exception():
    with pytest.raises(IndexError):
        with Suppressor(ZeroDivisionError):
            [0][1]
