import sys


def test_cmatools_installed():
    """ Test to verify that the cmatools package has been installed and can be imported """

    try:
        import cmatools

        print(f"cmatools version: {cmatools.__version__}")
    except ImportError as e:
        print("cmatools was not available for import")
        print(e)
        print("Try re-installing the system, ensure cmatools package is available")
    assert ("cmatools" in sys.modules) is True
