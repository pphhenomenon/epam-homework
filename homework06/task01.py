"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.created_instances = 0

    def __new__(cls):
        cls.created_instances += 1
        return super(cls, cls).__new__(cls)

    @classmethod
    def get_created_instances(cls):
        return cls.created_instances

    @classmethod
    def reset_instances_counter(cls):
        counter, cls.created_instances = cls.created_instances, 0
        return counter

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class SomeClass:
    ...


if __name__ == "__main__":
    SomeClass.get_created_instances()
    instance, *_ = SomeClass(), SomeClass(), SomeClass()
    instance.get_created_instances()
    instance.reset_instances_counter()
    instance.get_created_instances()
