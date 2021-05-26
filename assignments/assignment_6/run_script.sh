#!/usr/bin/env bash
#Environment name
VENVNAME=as6env

#Activate environment
python3 -m venv $VENVNAME
source $VENVNAME/bin/activate

#Upgrade pip
pip install --upgrade pip

# problems when installing from requirements.txt
test -f requirements.txt && pip install -r requirements.txt

#Change directory to data folder
cd src

#Run the scripts
python LogisticRegression.py $@
python DL_model.py $@

deactivate
