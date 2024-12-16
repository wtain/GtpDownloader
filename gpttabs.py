
import urllib.request
import urllib.parse

from httpclienthelpers import download_file
from scrappinghelpers import get_document, BasicScraper


class GPTTabsScraper(BasicScraper):

    def __init__(self):
        BasicScraper.__init__(self, "https://gtptabs.com", "gpttabs")

    def get_base_path(self, query):
        query_encoded = urllib.parse.quote_plus(query)
        return f"/search/go.html?SearchForm%5BsearchString%5D={query_encoded}&SearchForm%5BsearchIn%5D=tab&yt0=Find"

    def download_tabs(self, query, output_dir):
        BasicScraper.download_tabs(self, query, output_dir)

        base_path = self.get_base_path(query)

        URL = f'{self.BASE_URL}{base_path}'

        document = get_document(URL)
        autorSongs = document.find('div', class_='autorSongs')
        children = autorSongs.findAll('div', class_='title')

        for div in children:
            title = div.find('a')
            href = title.attrs["href"]
            document1 = get_document(f"{self.BASE_URL}{href}")
            dlbutton = document1.find('a', class_='dlFile')
            href2 = dlbutton.attrs["href"]

            download_file(f'{self.BASE_URL}{href2}', output_dir)