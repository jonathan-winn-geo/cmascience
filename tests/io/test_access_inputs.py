from cmascience.io import access_input_urls


def test_access_input_urls():
    "test docstring"
    for url in access_input_urls.access_input_urls():
        assert url == 200
