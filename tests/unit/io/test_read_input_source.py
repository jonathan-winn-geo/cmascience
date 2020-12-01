from cmascience.io import read_input_source


def test_read_input_source():
    assert read_input_source.read_input_source_ini() == (
        "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_coastline.zip",
        "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_coastline.zip",
        "https://www.metoffice.gov.uk/hadobs/hadsst4/data/netcdf/HadSST.4.0.0.0_median.nc",
    )
