import requests

from cmascience.io.read_input_source import read_input_source_ini


def access_input_urls():
    codes = []
    for url in read_input_source_ini():
        resp = requests.head(url, allow_redirects=True)
        codes.append(resp.status_code)
    return codes