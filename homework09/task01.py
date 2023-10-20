"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""


from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def unpacking(filename: str) -> Iterator[int]:
    with open(filename) as filedata:
        yield from (int(data) for data in filedata)


def merge_sorted_files(filelist: List[Union[Path, str]]) -> Iterator[int]:
    iterators = (unpacking(filename) for filename in filelist)
    yield from merge(*iterators)
