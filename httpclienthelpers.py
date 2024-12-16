import re
from urllib.request import Request, urlopen

def get_file_name_from_headers(url_opener):
    content_disposition = \
        list(map(lambda t: t[1], filter(lambda t: t[0] == 'Content-Disposition', url_opener.getheaders())))[0]
    m = re.search(r"filename=(.+)", content_disposition)
    return m[1].strip('\"')

def download_file(url, output_dir, referer=None):
    print(f"*** Downloading from {url} to {output_dir}")
    req = Request(url)
    if referer:
        req.add_header('Referer', referer)
    with urlopen(req) as url_opener:
        data = url_opener.read()
        file_name = get_file_name_from_headers(url_opener)
        with open(f"{output_dir}/{file_name}", 'wb') as out:
            out.write(data)