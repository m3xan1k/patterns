from __future__ import annotations
import urllib.request


class DownloaderMeta(type):

    _instance: Downloader = None
    
    def __call__(self) -> Downloader:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance
        
        
class Downloader(metaclass=DownloaderMeta):
    @staticmethod
    def get(url):
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf-8')


if __name__ == '__main__':
    d1 = Downloader()
    d2 = Downloader()
    
    print(id(d1) == id(d2))

    html = d1.get('http://example.com')
    print(html)
