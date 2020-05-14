#!/bin/bash

codedir="$(dirname "$PWD")"
echo "$codedir"

black $codedir/cmascience
black $codedir/tests