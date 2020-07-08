from cmascience.io.download_inputs import download_input_data
from cmascience.io.filename_from_url import return_filename

def test_return_filename():
    "test docstring"
    url = "https://www.metoffice.gov.uk/hadobs/hadsst4/data/netcdf/HadSST.4.0.0.0_median.nc"

    result = return_filename(url)
    assert type(result) is str
