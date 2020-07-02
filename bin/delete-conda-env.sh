#!/bin/bash

# Script to delete current conda environment
# Used to re-set the system , e.g. prior to a new full installation

source $(conda info --base)/etc/profile.d/conda.sh

conda deactivate

while true; do
    read -p "Do you want to delete the current conda environment?" yn
    case $yn in
        [Yy]* ) echo "Removing the conda environment";
          echo "This is a slow process, please be patient";
          conda remove --name cmascience-env --all;
          break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done