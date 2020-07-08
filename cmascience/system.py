#!/usr/bin/env python3

from cmascience.io.download_inputs import download_input_data
from cmascience.io.read_root_dir import return_root_dir
from cmascience.io.verify_datadir import datadir


return_root_dir()
datadir()
download_input_data()


