from typing import Union

import pytest

from homework08.task01 import KeyValueStorage


@pytest.fixture
def userfile(request, tmpdir) -> str:
    """Custom fixture that creates a temporary file.

    Arguments:
        request (fixture): provides information of the requesting test function
        tmpdir (fixture): provides a temporary directory

    Returns:
        str: full path to the file
    """
    file = tmpdir.join('text.txt')
    file.write(request.param)
    return file.strpath


@pytest.mark.parametrize(
    'userfile',
    [
        'name=kek\n'
        'last_name=top\n'
        'power=9001\n'
        'song_name=shadilay\n'
    ],
    indirect=True,
)
@pytest.mark.parametrize(
    'item, value',
    [
        ['name', 'kek'],
        ['last_name', 'top'],
        ['power', 9001],
        ['song_name', 'shadilay'],
    ],
)
def test_accessible_as_collection(
    userfile: str, item: str, value: Union[str, int]
):
    """Tests `KeyValueStorage` class for getting values as collection items.

    Arguments:
        userfile (str): full path to the data file
        item (str): collectiom item
        value (Union[str, int]): collection value
    """
    storage = KeyValueStorage(userfile)
    assert storage[item] == value


@pytest.mark.parametrize(
    'userfile',
    [
        'name=kek\n'
        'last_name=top\n'
        'power=9001\n'
        'song_name=shadilay\n'
    ],
    indirect=True,
)
@pytest.mark.parametrize(
    'item, value',
    [
        ['name', 'kek'],
        ['last_name', 'top'],
        ['power', 9001],
        ['song_name', 'shadilay'],
    ],
)
def test_accessible_as_attribute(
    userfile: str, item: str, value: Union[str, int]
):
    """Tests `KeyValueStorage` class for getting values as attributes.

    Arguments:
        userfile (str): full path to the data file
        item (str): attribute
        value (Union[str, int]): attribute value
    """
    storage = KeyValueStorage(userfile)
    assert getattr(storage, item) == value


@pytest.mark.parametrize(
    'userfile',
    [
        '__doc__=kek\n'
        '__repr__=top\n'
        '__dict__=9001\n'
        '__class__=shadilay\n'
    ],
    indirect=True,
)
@pytest.mark.parametrize(
    'item, value',
    [
        ['__doc__', 'kek'],
        ['__repr__', 'top'],
        ['__dict__', 9001],
        ['__class__', 'shadilay'],
    ],
)
def test_builtin_attributes(
    userfile: str, item: str, value: Union[str, int]
):
    """Tests `KeyValueStorage` class for built-in attributes.

    Arguments:
        userfile (str): full path to the data file
        item (str): attribute
        value (Union[str, int]): attribute value
    """
    storage = KeyValueStorage(userfile)
    assert getattr(storage, item) != value
