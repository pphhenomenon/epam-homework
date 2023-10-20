from homework06.task01 import instances_counter


@instances_counter
class SomeClass:
    ...


def test_get_created_instances():
    assert SomeClass.get_created_instances() == 0
    instance = SomeClass()
    assert instance.get_created_instances() == 1
    other_instance = SomeClass()
    assert other_instance.get_created_instances() == 2


def test_reset_instances_counter():
    instance, *_ = SomeClass(), SomeClass(), SomeClass()
    assert instance.get_created_instances() == 5
    assert instance.reset_instances_counter() == 5
    assert instance.get_created_instances() == 0
