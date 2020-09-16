import requests
import re

from requests.exceptions import RequestException


def return_filename(url):

    try:
        with requests.get(url) as r:

            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = url.split("/")[-1]

            print(fname)
            return fname
    except RequestException as e:
        print(e)
