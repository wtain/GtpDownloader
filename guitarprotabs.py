
from httpclienthelpers import download_file
from scrappinghelpers import get_document, BasicScraper


class GuitarProTabsScraper(BasicScraper):

    def __init__(self):
        BasicScraper.__init__(self, "https://guitarprotabs.org/", "guitarprotabs")

    def get_base_path(self, query):
        query_lower = query.lower()
        query_lower_no_spaces = query_lower.replace(' ', '_')
        first_character = query_lower_no_spaces[0]

        return f"{first_character}/{query_lower_no_spaces}"

    def download_tabs(self, query, output_dir):
        BasicScraper.download_tabs(self, query, output_dir)

        base_path = self.get_base_path(query)

        page = 1
        while True:
            url = f"{self.BASE_URL}{base_path}/{page}/"

            print(f"*** Page {page}")

            document = get_document(url)
            table = document.find('table', class_='table')
            if not table:
                break
            tbody = table.find("tbody")
            tr_list = tbody.findChildren('tr')
            should_continue = False
            for tr in tr_list:
                a = tr.find('a')
                if not a:
                    break
                href = a.attrs["href"]

                document_child = get_document(href)
                download_div = document_child.find('div', class_='download-cta')
                btn_info = download_div.find('a', class_='btn-info')
                download_url = btn_info.attrs["href"]
                download_file(download_url, output_dir, href)
                should_continue = True

            if not should_continue:
                break

            page += 1
