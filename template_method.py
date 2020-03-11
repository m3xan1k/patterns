from abc import ABC, abstractmethod
import urllib3
from typing import Any, List
import io


class AbstractRequester(ABC):
    def template_method(self, data):
        urls = self.get_urls(data)
        for url in urls:
            response = self.make_request(url)
            print(response.status)

    def make_request(self, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        return response

    @abstractmethod
    def get_urls(self, data: Any) -> list:
        pass


class DictRequester(AbstractRequester):
    def get_urls(self, data: List[dict]) -> list:
        return [item['url'] for item in data]


class FileRequester(AbstractRequester):
    def get_urls(self, data: str) -> list:
        f = io.StringIO(data)
        content = f.read()
        return [url.strip() for url in content.split('\n') if url]


if __name__ == '__main__':
    DictRequester().template_method([{'url': 'https://example.com'}, {'url': 'https://github.com'}])

    data = 'https://webscraper.io/test-sites/e-commerce/allinone\nhttps://example.org\n'
    FileRequester().template_method(data)
