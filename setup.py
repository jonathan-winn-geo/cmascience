import setuptools

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
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data = True,
    package_data = {
        # Ensure config.ini file is available within installed package
        # If any package contains *.ini files, include them
        '': ['*.ini']
    },
    install_requires=[
                      "cmatools @ git+https://github.com/cma-open/cmatools",
                     # "package2 @ git+https://github.com/user2/package2@branch1",

                      ],

    # entry_points
)