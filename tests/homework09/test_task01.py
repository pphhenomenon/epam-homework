import pytest

from homework09.task01 import merge_sorted_files


@pytest.mark.parametrize(
    'filelist',
    [
        [['1', '3', '5'], ['2', '4', '6']],
        [['1', '4', '6'], ['2', '3', '5']],
        [['2', '3', '5'], ['1', '4', '6']],
    ]
)
def test_merge_sorted_files(filelist, tmpdir):
    for i, filedata in enumerate(filelist):
        tmpdir.join('{}'.format(i)).write('\n'.join(filedata))
    assert list(merge_sorted_files(tmpdir.listdir())) == [1, 2, 3, 4, 5, 6]
