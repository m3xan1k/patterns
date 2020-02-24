from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def calculate_trip(self, miles: int, passengers: int) -> str:
        trip = self.factory_method()
        price = trip.calculate_price(miles, passengers)
        time = trip.calculate_time(miles)
        return f'time: {time}, price: {price}'


class CarTripFactory(Factory):
    def factory_method(self) -> CarTrip:
        return CarTrip()


class AirTripFactory(Factory):
    def factory_method(self) -> AirTrip:
        return AirTrip()


class Trip(ABC):

    @abstractmethod
    def calculate_price(self):
        pass

    @classmethod
    def calculate_time(cls, miles: int) -> float:
        return miles / cls.time_multiplier / 60


class CarTrip(Trip):
    price_multiplier = 4
    time_multiplier = 1.6

    @classmethod
    def calculate_price(cls, miles: int, passengers: int) -> float:
        return miles * cls.price_multiplier


class AirTrip(Trip):
    price_multiplier = 3
    time_multiplier = 7.6

    @classmethod
    def calculate_price(cls, miles: int, passengers: int) -> float:
        return miles * passengers * cls.price_multiplier


if __name__ == '__main__':
    miles = 700
    passengers = 2

    car_trip = CarTripFactory()
    car_result = car_trip.calculate_trip(miles, passengers)
    print(car_result)

    air_trip = AirTripFactory()
    air_result = air_trip.calculate_trip(miles, passengers)
    print(air_result)
