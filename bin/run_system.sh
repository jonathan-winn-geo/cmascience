#!/bin/bash

packagedir="$(dirname "$PWD")"
echo "$packagedir"

python3 $packagedir/cmascience/system.py

