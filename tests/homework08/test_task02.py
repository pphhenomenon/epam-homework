import pytest

from homework08.task02 import TableData


@pytest.fixture
def presidents():
    return TableData('tests/homework08/database.db', 'presidents')


def test_len(presidents):
    assert len(presidents) == 3


def test_contains(presidents):
    for president in presidents:
        assert president['name'] in presidents


def test_collection(presidents):
    for president in presidents:
        assert presidents[president['name']] == tuple(president)


def test_iterator(presidents):
    for president in presidents:
        assert president['name'] in [
            president['name'] for president in presidents
        ]
