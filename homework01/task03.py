from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:

    """Returns a tuple with the min and max values of input file
    which contains line-delimited integers."""

    with open(file_name) as data:
        min_num = int(data.readline())
        max_num = min_num

        for line in data:
            num = int(line)

            if num < min_num:
                min_num = num
            elif num > max_num:
                max_num = num

    return min_num, max_num
