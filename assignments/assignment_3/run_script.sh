#!/usr/bin/env bash

#Environment name
VENVNAME=as3env

#Create and Activate environment
python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip
pip install spacy
python -m spacy download en_core_web_sm


# problems when installing from requirements.txt
test -f requirements.txt && pip install -r requirements.txt
#unzip the data 
cd data 
unzip a_million_headlines.zip
cd ..

#navigate to src folder
cd src
#create the data scores for the headlines, this takes a while (~15 min) 
python data_setup.py $@
#run script
python sentiment_analysis.py $@ 

#deactivate environment
deactivate
