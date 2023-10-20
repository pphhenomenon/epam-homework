from typing import Union


class KeyValueStorage:
    __storage = {}

    def __init__(self, filepath: str):
        """Constructor.

        Arguments:
            filepath (str): file that works as key-value storage

        Raises:
            ValueError: if the value cannot be assigned to an attribute,
                if the attribute conflicts with existing built-in attributes
        """
        with open(filepath) as lines:
            for line in lines:
                item, value = line.strip().split("=")
                if not item.isidentifier():
                    raise ValueError("invalid attribute: '{}'".format(item))
                if item in self.__class__.__dict__ or item in self.__dict__:
                    continue
                value = int(value) if value.isdigit() else value
                self.__storage[item] = value

    def __getitem__(self, item: str) -> Union[str, int]:
        """Allows getting values as items of a collection.

        Arguments:
            item (str): collection item

        Returns:
            Union[str, int]: collection value
        """
        if hasattr(self, item):
            return getattr(self, item)
        return self.__storage[item]

    def __getattr__(self, item: str) -> Union[str, int]:
        """Allows getting values as attributes.

        Arguments:
            item (str): attribute

        Returns:
            Union[str, int]: attribute value
        """
        return self.__storage[item]
