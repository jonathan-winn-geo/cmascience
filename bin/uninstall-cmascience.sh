#!/bin/bash

# Uninstall hadcrut package
# Deletes local install files and directories

COD_DIR="$(dirname "$PWD")"
echo "$CODE_DIR"
pip uninstall -y cmascience
echo "Removing .egg-info directory"
rm -rf $CODE_DIR/build
echo "Removing build directory"
rm -rf $CODE_DIR/cmascience.egg-info