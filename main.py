from gprotabnet import GproTabNetScraper
from gpttabs import GPTTabsScraper
from guitarprotabs import GuitarProTabsScraper


band_name = "children of bodom"

scrapers = [
    GPTTabsScraper(),
    GuitarProTabsScraper(),
    GproTabNetScraper(),
]

for scraper in scrapers:
    print(f"*** Running {scraper.get_name()} scraper")
    scraper.download_tabs(band_name, f'download/{scraper.get_name()}/{band_name}')