from math import sqrt
from typing import Generator, Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Returns if the given sequence is a Fibonacci sequence."""

    def is_square(num: int):
        """Returns if the given number is a perfect square."""
        return num == int(sqrt(num)) ** 2

    def is_valid(num: int):
        """Returns if the given number is a Fibonacci number."""
        return is_square(5 * num ** 2 + 4) or is_square(5 * num ** 2 - 4)

    if isinstance(data, str):
        data = tuple(map(int, data.split(",")))

    if tuple(data) in ((0, 1), (1, 1)):
        return True

    if len(data) == 1:
        return is_valid(data[0])

    if len(data) == 2:
        extended = [data[1] - data[0], data[0], data[1]]

        if extended != sorted(extended) or len(set(data)) != len(data):
            return False
        return all(map(is_valid, data))

    for i in range(len(data) - 2):
        if not data[i] + data[i + 1] == data[i + 2] or not is_valid(data[i]):
            return False
    return True


def fibonacci_generator(
    start_number: int, current_number: int = 0, next_number: int = 1
) -> Generator[int, None, None]:
    while True:
        if current_number >= start_number:
            yield current_number
        current_number, next_number = next_number, current_number + next_number


def check_fibonacci_other_solution(data: Sequence[int]) -> bool:
    start_element = next(iter(data), None)
    if start_element is None:
        return False
    for our_element, true_element in zip(
        data, fibonacci_generator(start_element)
    ):
        if our_element != true_element:
            return False
    return True
