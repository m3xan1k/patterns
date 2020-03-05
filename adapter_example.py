import requests
import urllib3


class Downloader:
    """
    Старый загрузчик системы
    """
    def request(self, url: str) -> bytes:
        return requests.get(url).content


class CustomDownloader:
    """
    Новый загрузчик, который нужно интегрировать в систему
    """
    def make_custom_request(self, url: str) -> bytes:
        client = urllib3.PoolManager()
        return client.request('GET', url).data


class DownloaderAdapter(Downloader):
    """
    Адаптер для создания совместимости
    старого кода и нового загрузчика
    """
    def __init__(self, adaptee: CustomDownloader) -> None:
        self.adaptee = adaptee
    
    def request(self, url) -> bytes:
        return self.adaptee.make_custom_request(url)


def code(target: Downloader, url: str) -> None:
    """
    Старая функция
    """
    print(target.request(url).decode('utf-8'))


if __name__ == '__main__':
    adaptee = CustomDownloader()
    adapter = DownloaderAdapter(adaptee)
    code(target=adapter, url='http://example.com')
