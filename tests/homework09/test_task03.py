from pathlib import Path

import pytest

from homework09.task03 import universal_file_counter


@pytest.fixture
def dirpath(request, tmpdir):
    for i, filedata in enumerate(request.param):
        tmpdir.join('{}.txt'.format(i)).write('\n'.join(filedata))
    return Path(tmpdir)


@pytest.mark.parametrize(
    'dirpath',
    [
        [['1', '3', '5'], ['2', '4', '6']],
    ],
    indirect=True,
)
def test_merge_sorted_files(dirpath):
    assert universal_file_counter(dirpath, 'txt') == 6


@pytest.mark.parametrize(
    'dirpath',
    [
        [['1 3 5', '2 4 6'], ['4 7 9', '3 6 8']],
    ],
    indirect=True,
)
def test_merge_sorted_files_with_tokenizer(dirpath):
    assert universal_file_counter(dirpath, 'txt', str.split) == 12
