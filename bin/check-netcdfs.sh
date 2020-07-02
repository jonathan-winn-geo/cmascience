#!/bin/bash


CODE_DIR="$(dirname "$PWD")"
echo "$CODE_DIR"

DATA=$CODE_DIR/data/reference

TEST_FILE="tos_O1_2001-2002.nc"
TEST_FILE_2="sresa1b_ncar_ccsm3-example.nc"

compliance-checker --test=cf --verbose $DATA/$TEST_FILE $DATA/$TEST_FILE_2

# compliance-checker --test=cf:1.7 $DATA/$TEST_FILE

# output to file
# compliance-checker --test=acdd:1.3 --format=text --output=/tmp/report.txt compliance_checker/tests/data/examples/hycom_global.nc

echo " ------------"
echo " ------------"
echo " ------------"

cfchecks $DATA/$TEST_FILE $DATA/$TEST_FILE_2
