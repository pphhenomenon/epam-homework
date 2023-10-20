import datetime

from homework05.task01 import Student, Teacher


def teacher():
    return Teacher("Nikita", "Trofimov")


def student():
    return Student("Elvin", "Guliev")


def test_teacher_attributes():
    assert teacher().first_name == "Nikita" and \
        teacher().last_name == "Trofimov"


def test_student_attributes():
    assert student().first_name == "Elvin" and \
        student().last_name == "Guliev"


def test_create_homework_attributes():
    expired_homework = teacher().create_homework("Solve the equation", 0)
    assert expired_homework.text == "Solve the equation" and \
        expired_homework.deadline == datetime.timedelta(0)


def test_function_create_homework():
    create_homework_ = teacher().create_homework
    current_homework = create_homework_("Study the topic", 5)
    assert current_homework.text == "Study the topic" and \
        current_homework.deadline == datetime.timedelta(5)


def test_active_homework():
    current_homework = teacher().create_homework("Solve the problem", 5)
    assert student().do_homework(current_homework) == current_homework


def test_expired_homework():
    expired_homework = teacher().create_homework("Learn the function", 0)
    assert student().do_homework(expired_homework) is None
