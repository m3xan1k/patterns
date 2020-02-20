from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

import requests


class Publisher(ABC):
    """
    Субъект или издатель в терминологии паттерна
    """
    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class AvailabilityChecker(Publisher):
    """
    Конкретная реализация субъекта
    """
    _state = None
    _observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    """
    Бизнес-логика
    """
    def check(self):
        r = requests.get('https://example.com')
        self._state = r.status_code
        self.notify()


class Observer(ABC):
    """
    Интерфейс абстрактного наблюдателя
    """
    def update(self, subject: Publisher) -> None:
        pass


class EventListenerA(Observer):
    """
    Реализация конкретного наблюдателя
    """
    def update(self, subject: Publisher) -> None:
        if subject._state == 200:
            print('Site is available')
        else:
            print('Site is unavailable')


class EventListenerB(Observer):
    """
    Реализация конкретного наблюдателя
    """
    def update(self, subject: Publisher) -> None:
        if subject._state == 200:
            r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
            print(r.json())
        else:
            print('Non internet connection')


if __name__ == '__main__':
    checker = AvailabilityChecker()
    listener_a = EventListenerA()
    listener_b = EventListenerB()

    for listener in [listener_a, listener_b]:
        checker.subscribe(listener)

    checker.check()
