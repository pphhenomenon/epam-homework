from homework03.task02 import fast_calculate


def test_regular_case():
    """Tests the fast_calculation function.

    Here we decided to compare the result of the fast function with the
    correct solution instead of comparing it with the slow function, because
    the execution of the slow function takes a long time.

    :return: the truth of an expression
    :rtype: bool
    """
    assert fast_calculate(range(500)) == 1024259
