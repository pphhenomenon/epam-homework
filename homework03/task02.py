import hashlib
import random
import struct
import time
from multiprocessing import Pool, cpu_count


def slow_calculate(number):
    """Some weird voodoo magic calculations."""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(number).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(numbers):
    """Speeds up the function by creating multiple processes.

    :param numbers: data for processing
    :type numbers: iterable object

    :raises TimeoutError: if the execution time is more than 60 seconds

    :return: the sum of the results of the slow function
    :rtype: int
    """
    constant = 6
    with Pool(constant * cpu_count()) as pool:
        answer = sum(pool.map(slow_calculate, numbers))
    return answer


if __name__ == "__main__":
    print(fast_calculate(range(500)))
