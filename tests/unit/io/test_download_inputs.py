from cmascience.io.download_inputs import download_input_data


def test_download_inputs():
    "test docstring"
    for status in download_input_data():
        assert status == 200
