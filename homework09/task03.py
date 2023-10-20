"""  # noqa: E501
Write a function that takes directory path, file extension and an optional tokenizer.
It will count lines in all files with that extension if there is no tokenizer.
If the tokenizer is not none, it will count tokens.

For the directory with 2 files from task01.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""


from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dirpath: Path, extension: str, tokenizer: Optional[Callable] = None
) -> int:

    counter = 0

    for file in dirpath.glob('*.{}'.format(extension)):
        with open(file) as filedata:
            if callable(tokenizer):
                for line in filedata:
                    counter += len(tokenizer(line.strip()))
            if tokenizer is None:
                counter += sum(1 for line in filedata)

    return counter
