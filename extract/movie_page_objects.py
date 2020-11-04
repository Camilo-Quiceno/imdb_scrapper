import requests
import lxml.html as html

from common import config

class StorePage:

    def __init__(self, movie_site_id, url):

        self._config = config()['movie_site'][movie_site_id]
        self._queries = self._config['queries']
        self._html = None
        self._url = url

        self._visit(url)

    def _select(self, query_string):
        return self._html.xpath(query_string)

    def _visit(self,url):

        response = requests.get(url)

        if response.status_code == 200:

            home = response.content.decode('utf-8')
            self._html = html.fromstring(home)

class HomePage(StorePage):
    def __init__(self, movie_site_id, url):
        super().__init__(movie_site_id, url)

    @property
    def movie_links(self):
        movie_links = []
        for link in self._select(self._queries['home_movie_links']):
            movie_links.append(link)
            
           
        return movie_links