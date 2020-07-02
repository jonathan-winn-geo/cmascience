import requests
from cmascience.io.read_input_source import read_input_source_ini


def test_input_headers():
    "test docstring"
    for url in read_input_source_ini():
        resp = requests.get(url, allow_redirects=True)
        print(url)
        for x, y in resp.headers.items():
            print(x, y)


#TODO check re log options, add header details to the log, for later metadata ref