from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCoffee(ABC):
    @abstractmethod
    def __init__(self):
        self._description = None

    @abstractmethod
    def get_description(self):
        return self._description

    @abstractmethod
    def get_cost(self):
        pass


class AddOn(ABC):
    @abstractmethod
    def __init__(self, coffee: AbstractCoffee):
        self._coffee = coffee

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class Espresso(AbstractCoffee):
    def __init__(self):
        self._description = 'Espresso coffee'

    def get_description(self):
        return self.get_description()

    def get_cost(self):
        return 1.99


class HouseBlend(AbstractCoffee):
    def __init__(self):
        self._description = 'House Blend Coffee'

    def get_description(self):
        return self._description

    def get_cost(self):
        return 0.89


class Milk(AddOn):
    def __init__(self, coffee: AbstractCoffee):
        self._coffee = coffee

    def get_description(self):
        return self._coffee.get_description() + ', Milk'

    def get_cost(self):
        return 0.20 + self._coffee.get_cost()


class Sugar(AddOn):
    def __init__(self, coffee: AbstractCoffee):
        self._coffee = coffee

    def get_description(self):
        return self._coffee.get_description() + ', Sugar'

    def get_cost(self):
        return 0.1 + self._coffee.get_cost()

if __name__ == '__main__':
    my_coffee = HouseBlend()
    print(my_coffee.get_description(), my_coffee.get_cost())
    my_coffee = Milk(my_coffee)
    print(my_coffee.get_description(), my_coffee.get_cost())
    my_coffee = Sugar(my_coffee)
    print(my_coffee.get_description(), my_coffee.get_cost())
