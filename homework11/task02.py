"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75

order_2 = Order(100, evening_discount)
assert order_2.final_price() == 10
"""


class DiscountStrategyContext:

    @staticmethod
    def __check_discount(order, discount):
        if discount and discount(order) < 0:
            raise ValueError('discount cannot be more than 100 percent')

    def __set_name__(self, type, name):
        self.name = '__{}'.format(name)

    def __get__(self, instance, type):
        return getattr(instance, self.name)

    def __set__(self, instance, strategy):
        self.__check_discount(instance, strategy)
        setattr(instance, self.name, strategy)


class Order:
    discount = DiscountStrategyContext()

    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def final_price(self):
        if self.discount:
            return self.discount(self)
        return self.price
