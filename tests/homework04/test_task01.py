import pytest

from homework04.task01 import read_magic_number


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test.txt"


def test_positive_case(temp_file):
    temp_file.write_text("2\n5\n7\n3\nt\np\nd")
    assert read_magic_number(temp_file)


def test_negative_case(temp_file):
    temp_file.write_text("4\n5\n7\n3\nt\np\nd")
    assert not read_magic_number(temp_file)


def test_value_error_case(temp_file):
    temp_file.write_text("a\n5\n7\n3\nt\np\nd")
    with pytest.raises(ValueError, match="could not convert to float number"):
        read_magic_number(temp_file)
