#!/bin/bash

CODE_DIR="$(dirname "$PWD")"
echo "$CODE_DIR"

DATA=$CODE_DIR/data/reference

TEST_FILE="tos_O1_2001-2002.nc"
TEST_FILE_2="sresa1b_ncar_ccsm3-example.nc"
TEST_FILE_3="HadSST.4.0.0.0_median.nc"

# ncdump -c $DATA/$TEST_FILE

ncdump -c $DATA/$TEST_FILE

echo "------"

ncdump -c $DATA/$TEST_FILE_2

echo "------"

ncdump -c $DATA/$TEST_FILE_3