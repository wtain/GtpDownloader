from httpclienthelpers import download_file
from scrappinghelpers import get_document, get_element_attribute_by_inner_text, BasicScraper


class GproTabNetScraper(BasicScraper):

    def __init__(self):
        BasicScraper.__init__(self, 'https://gprotab.net', "gprotabnet")

    def get_base_path(self, query):
        query_lower = query.lower()
        query_lower_no_spaces = query_lower.replace(' ', '-')
        return f"/en/tabs/{query_lower_no_spaces}"

    def download_tabs(self, query, output_dir):
        BasicScraper.download_tabs(self, query, output_dir)

        base_path = self.get_base_path(query)

        document = get_document(f"{self.BASE_URL}{base_path}")
        ul_list = document.findChildren('ul', class_='tabs')
        for ul in ul_list:
            li_list = ul.findChildren('li')
            for li in li_list:
                a = li.find('a')
                href = a.attrs['href']

                document_child = get_document(f"{self.BASE_URL}{href}")
                div = document_child.find('div', class_='tab-data')
                all_a = div.findChildren('a')
                href = get_element_attribute_by_inner_text(all_a, "href", "Download")
                download_file(f"{self.BASE_URL}{href}", output_dir)