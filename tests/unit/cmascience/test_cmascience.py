import sys


def test_cmascience_installed():
    """Test to verify that the package has been installed and can be imported."""
    try:
        import cmascience

        print(f"cmascience version: {cmascience.__version__}")
    except ImportError as e:
        print("cmascience was not available for import")
        print(e)
        print("Try re-installing the system, ensure the package is available")
    assert ("cmascience" in sys.modules) is True
