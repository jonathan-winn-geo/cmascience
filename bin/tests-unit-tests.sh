#!/bin/bash

testdir="$(dirname "$PWD")"
echo "$testdir"

# Discover and run tests on code path,  -v verbose flag
#python3 -m pytest -v --capture=tee-sys  $testdir
pytest -v --capture=tee-sys -rA  $testdir
