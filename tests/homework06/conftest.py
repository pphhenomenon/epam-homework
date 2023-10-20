import pytest

from homework06.task02 import Student, Teacher


@pytest.fixture
def teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture
def advanced_teacher():
    return Teacher("Aleksandr", "Smetanin")


@pytest.fixture
def lazy_student():
    return Student("Roman", "Petrov")


@pytest.fixture
def good_student():
    return Student("Lev", "Sokolov")


@pytest.fixture
def expired_homework(teacher: Teacher):
    return teacher.create_homework("Learn functions", 0)


@pytest.fixture
def homework(teacher: Teacher):
    return teacher.create_homework("Learn OOP", 1)


@pytest.fixture
def docs_homework(teacher: Teacher):
    return teacher.create_homework("Read docs", 5)
