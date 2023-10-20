import pytest

from homework11.task02 import Order


def morning_discount(order: Order) -> float:
    discount = 0.25
    return order.price - order.price * discount


def evening_discount(order: Order) -> float:
    discount = 0.75
    return order.price - order.price * discount


@pytest.mark.parametrize(
    'price, strategy, expected',
    [
        [100, morning_discount, 75],
        [100, evening_discount, 25],
        [100, None, 100],
    ]
)
def test_order(price, strategy, expected):
    assert Order(price, strategy).final_price() == expected
