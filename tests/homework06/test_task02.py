import pytest

from homework06.task02 import (DeadlineError, Homework, HomeworkResult,
                               Student, Teacher)


def test_do_homework(good_student: Student, docs_homework: Homework):
    """Tests the `do_homework` function.

    Arguments:
        good_student (Student): `Student` instance
        docs_homework (Homework): `Homework` instance
    """
    homework = good_student.do_homework(docs_homework, "I have done this homework.")  # noqa: E501

    assert isinstance(homework, HomeworkResult)
    assert homework.author == good_student
    assert homework.solution == "I have done this homework."
    assert homework.homework == docs_homework


def test_deadline_error(lazy_student: Student, expired_homework: Homework):
    """Tests the `do_homework` function that raises `DeadlineError` expection.

    Arguments:
        lazy_student (Student): `Student` instance
        expired_homework (Homework): `Homework` instance
    """
    with pytest.raises(DeadlineError) as error:
        lazy_student.do_homework(expired_homework, "Solution")
    assert str(error.value) == "You are late."


def test_homework_result(good_student: Student):
    """Tests the `HomeworkResult` class that raises a `TypeError` exception.

    Arguments:
        good_student (Student): `Student` instance
    """
    with pytest.raises(TypeError) as error:
        HomeworkResult(good_student, "Homework", "Solution")
    assert str(error.value) == "It's not Homework object."


def test_check_homework(
    teacher: Teacher, good_student: Student, homework: Homework
):
    """Tests the `check_homework` function.

    Arguments:
        teacher (Teacher): `Teacher` instance
        good_student (Student): `Student` instance
        homework (Homework): `Homework` instance
    """
    result = good_student.do_homework(homework, "I have done this homework.")

    assert teacher.check_homework(result)
    assert result.homework in teacher.homework_done


def test_reset_result(
    teacher: Teacher, good_student: Student, homework: Homework
):
    """Tests the `reset_result` function.

    Arguments:
        teacher (Teacher): `Teacher` instance
        good_student (Student): `Student` instance
        homework (Homework): `Homework` instance
    """
    result = good_student.do_homework(homework, "I have done this homework.")
    teacher.check_homework(result)

    teacher.reset_results(homework)
    assert len(teacher.homework_done) == 1

    # The length of the `homework_done` dictionary is equal to one, because
    # one homework was already added to the `homework_done` dictionary when
    # the `test_check_homework` function was runned.

    teacher.reset_results()
    assert len(teacher.homework_done) == 0


def test_check_homework_unique_solution(
    good_student: Student, homework: Homework, teacher: Teacher
):
    """Tests the `check_homework` function for the absence of duplicate
    elements in the `homework_done` dictionary for each homework.

    Arguments:
        good_student (Student): `Student` instance
        homework (Homework): `Homework` instance
        teacher (Teacher): `Teacher` instance
    """
    result = good_student.do_homework(homework, "I have done this homework.")
    result_ = good_student.do_homework(homework, "I have done this homework.")

    teacher.check_homework(result)
    teacher.check_homework(result_)

    assert len(teacher.homework_done) == 1
