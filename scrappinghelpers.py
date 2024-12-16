import os
from abc import abstractmethod

import bs4
import requests


def get_document(url):
    html = requests.get(url).text
    return bs4.BeautifulSoup(html, 'html.parser')

def get_element_attribute_by_inner_text(element_list, attribute, inner_text):
    for a in element_list:
        if a.string == inner_text:
            return a.attrs[attribute]


class BasicScraper:

    def __init__(self, base_url, name):
        self.BASE_URL = base_url
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def get_base_path(self, query):
        pass

    def download_tabs(self, query, output_dir):
        os.makedirs(output_dir, exist_ok=True)