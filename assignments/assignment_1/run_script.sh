#!/usr/bin/env bash

#Environment name
VENVNAME=as1env

#Create and Activate environment
python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip
pip install pandas

# problems when installing from requirements.txt
test -f requirements.txt && pip install -r requirements.txt

#navigate to src folder
cd src

#run script
python 100_novels_script.py  

#deactivate environment
deactivate
