import setuptools

# Use the main readme file, for the package description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmascience",
    version="0.0.1",
    author="Jonathan Winn",
    author_email="jonathan.winn@metoffice.com",
    description="Training example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cma-open/cmascience",
    # Find and install all packages and subpackages
    # Alternatively packages to install can be named directly
    packages=setuptools.find_packages(),
    # Classifiers, mainly intended for use at upload to PyPi, but also useful for users
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
    ],
    # Prevent pip install from installing on earlier versions of python
    python_requires='>=3.7',
    # This tells setuptools to install any data files it finds in your packages.
    # The data files must be specified via the distutils’ MANIFEST.in file.
    include_package_data = True,
    # For finer-grained control over what files are included
    # (e.g. if you have documentation files in your package directories and want to exclude them from installation)
    # The package_data argument is a dictionary that maps from package names to lists of glob patterns.
    package_data = {
        # Ensure config.ini file is available within installed package
        # If any package contains *.ini files, include them
        '': ['*.ini']
    },
    # Specify minimum package dependencies list
    # Can be used to force other packages to be installed, if not already available locally
    install_requires=[
        "cmatools @ git+https://github.com/cma-open/cmatools",
        "numpy",
        "black",
        "pytest"],

    # dependency_links is required for github actions tests to work
    # dependency_links is required if installed via python setup.py install, not required for pip installs
    # link can specify version e.g. #egg=cmatools-0.0.1 or can be left as root package
    dependency_links=["git+https://github.com/cma-open/cmatools.git#egg=cmatools"],
    # dependency_links = ["git+https://github.com/cma-open/cmatools.git#egg=cmatools-0.0.1"]

    # Entry points for command-line scripts
    # Allows Python functions to be directly registered as command-line tools (to be callable by name)
    # Register the command-line scripts from the relevant package module and function
    entry_points = {
    'console_scripts': [
        # Name the tool, link to the package function
        'cli-simple='
        'cmascience.cli_simple:cli_simple_entry_point',
        # Name the tool, link to the package function
        'cli-datasets='
        'cmascience.cli_datasets:cli_datasets_entry_point',]
    }
)