from abc import ABC, abstractmethod

import requests


class Role(ABC):
    """
    Абстрактый интерфейс для работы с контекста с поведением
    """
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass


class RequestManager:
    """
    Интерфейс для клиентов
    """
    def __init__(self, role: Role):
        self._role = role

    @property
    def role(self) -> Role:
        return self._role

    @role.setter
    def role(self, role: Role) -> None:
        self._role = role

    def make_get_request(self, *args, **kwargs):
        return self._role.get(*args, **kwargs)

    def make_post_request(self, *args, **kwargs):
        return self._role.post(*args, **kwargs)


class SimpleDownload(Role):
    """
    Определяет поведение
    """
    def get(self, url: str, **kwargs) -> requests.Response:
        # здесь можно определить и более сложную логику с обработкой ошибок итд
        r = requests.get(url, **kwargs)
        return r

    def post(self, url: str, **kwargs) -> requests.Response:
        r = requests.post(url, **kwargs)
        return r


class SimpleSend(Role):
    """
    Определяет поведение
    """
    def post(self, url: str, data) -> requests.Response:
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, headers=headers, json=data)
        return r


class DownloadThroughProxy(Role):
    """
    Определяет поведение
    """
    # здесь можно инкапсулировать логику и методы работы с прокси
    proxies = {
        'http': 'http://example.com:1234',
        'https': 'http://example.com:1234',
    }

    def get(self, url: str, **kwargs):
        r = requests.get(url, proxies=self.proxies, **kwargs)
        return r

    def post(self, url: str, **kwargs):
        r = requests.get(url, proxies=self.proxies, **kwargs)
        return r


if __name__ == '__main__':
    manager = RequestManager(SimpleDownload())
    r = manager.make_get_request(url='https://example.com')
    print(r.text)
