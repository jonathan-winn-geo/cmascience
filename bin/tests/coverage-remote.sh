#!/bin/bash

rootdir="$(dirname $(dirname "$PWD"))"
testdir="$rootdir/tests"

echo "----------"
echo "$rootdir"
echo "$testdir"
echo "----------"

# Discover and run tests on code path,  -v verbose flag, with coverage stats
coverage run -m pytest -v $testdir

# Generate test report
coverage report -m