"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(cls, name: str, bases: tuple, attrs: dict):
        """Constructor that is responsible for creating the class.

        Arguments:
            name (str): class name
            bases (tuple): parent classes
            attrs (dict): attributes and methods contained in the class

        Returns:
            type: class
        """
        for item in attrs['_{}__keys'.format(name)]:
            attrs[item] = item
        return super().__new__(cls, name, bases, attrs)
