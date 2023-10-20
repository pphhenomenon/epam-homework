import pytest

from homework03.task03 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]


@pytest.mark.parametrize(
    "keywords, filtered",
    [
        ({"name": "Bill", "type": "person"}, [sample_data[0]]),
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
    ],
)
def test_regular_case(keywords, filtered):
    """Tests make_filter function on sample_data.

    :param keywords: filter parameters
    :type keywords: dict
    :param filtered: data filtered according to keywords
    :type filtered: list[dict]

    :return: boolean value
    :rtype: bool
    """
    assert make_filter(**keywords).apply(sample_data) == filtered
