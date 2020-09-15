#!/bin/bash

# Uninstall package
# Deletes local install files and directories

CODE_DIR="$(dirname "$PWD")"
echo "$CODE_DIR"

pip uninstall -y cmascience
pip uninstall -y cmatools

rm -rf $CODE_DIR/build
echo "Removing build directory"
rm -rf $CODE_DIR/cmascience.egg-info
echo "Removing .egg-info directory"