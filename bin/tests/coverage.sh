#!/bin/bash

rootdir="$(dirname $(dirname "$PWD"))"
testdir="$rootdir/tests"

echo "----------"
echo "$rootdir"
echo "$testdir"
echo "----------"

# Discover and run tests on code path,  -v verbose flag, with coverage stats
coverage run -m pytest -v --capture=tee-sys  $testdir
#--capture=tee-sys
# Generate test report
coverage report -m
coverage html
# Open test coverage report with firefox
firefox  htmlcov/index.html