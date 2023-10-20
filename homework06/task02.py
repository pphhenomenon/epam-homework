"""  # noqa: E501
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework).
Советую обратить внимание на defaultdict из модуля collection для
использования как общей переменной.


1. Как-то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult).

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки.
Атрибуты:
    homework - для объекта Homework, если передан не этот класс - выкинуть
    подходящее по смыслу исключение с сообщением:
    "You gave a not Homework object"

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено, то хотелось бы видеть исключение при do_homework,
а не просто принт "You are late".
Поднимайте исключение DeadlineError с сообщением "You are late" вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования.

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как у словаря, сюда попадают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гарантировать отсутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__ ...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True, если
    ответ студента больше 5 символов, также при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework, то удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названиям остальных переменных, классов и т. д. подходить ответственно -
давать логичные подходящие имена.
"""

from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):

    """Exception that raises when the homework has expired.
    """


class Person(object):

    """Class that represents a person.

    Attributes:
        first_name (str): Person's name
        last_name (str): Person's surname
    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Homework(object):

    """Class that represents a homework.

    Attributes:
        created (datetime): Homework creation time
        deadline (int): Homework deadline
        text (str): Homework description
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.now()

    def is_active(self):
        """Returns `True` if the homework is still relevant, `False` otherwise.

        Returns:
            bool: `True` if deadline hasn't come, `False` otherwise
        """
        return datetime.now() < self.deadline + self.created


class Student(Person):

    """Class that represents a student.
    """

    def do_homework(self, homework: Homework, solution: str):
        """Returns the `HomeworkResult` instance if the homework is still
        relevant, raise `DeadlineError` otherwise.

        Arguments:
            homework (Homework): `Homework` instance
            solution (str): Homework solution

        Returns:
            HomeworkResult: `HomeworkResult` instance

        Raises:
            DeadlineError: if homework is not relevant
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late.")


class HomeworkResult(object):

    """Class that represents successfully completed homeworks.

    Attributes:
        author (Studebt): `Student` instance
        created (datetime): Homework creation time
        homework (Homework): `Homework` instance
        solution (str): Homework solution
    """

    def __init__(self, author: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("It's not Homework object.")

        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.now()


class Teacher(Person):

    """Class that represents a teacher.

    Attributes:
        homework_done (defaultdict): Contains completed homeworks
    """

    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, deadline: int):
        """Returns the `Homework` instance.

        Arguments:
            text (str): Homework description
            deadline (int): Homework deadline

        Returns:
            Homework: `Homework` instance
        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, result: HomeworkResult):
        """If the student's solution is longer than 5 symbols, returns `True`
        and adds the homework to `homework_done`, `False` otherwise.

        Arguments:
            result (HomeworkResult): `HomeworkResult` instance

        Returns:
            bool: `True` if student's solution is longer than 5 symbols,
                `False` otherwise
        """
        if len(result.solution) > 5:
            cls.homework_done[result.homework].add(result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None):
        """If `Homework` instance is given, deletes all saved solutions
        in `homework_done` for this instance, clears `homework_done` otherwise.

        Arguments:
            homework (Homework, optional): `Homework` instance
        """
        if homework is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    advanced_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    homework = teacher.create_homework("Learn OOP", 1)
    docs_homework = teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(homework, "I have done this homework.")
    result_2 = good_student.do_homework(docs_homework, "I have done this homework.")  # noqa: E501
    result_3 = lazy_student.do_homework(docs_homework, "Done.")

    try:
        result_4 = HomeworkResult(good_student, "Homework", "Solution")
    except Exception:
        print("There was an exception here.")

    teacher.check_homework(result_1)
    temp_1 = teacher.homework_done

    advanced_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done

    assert temp_1 == temp_2

    teacher.check_homework(result_2)
    teacher.check_homework(result_3)

    print(Teacher.homework_done[homework])
    Teacher.reset_results()
