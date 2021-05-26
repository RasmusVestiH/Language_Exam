#!/usr/bin/env bash

#Environment name
VENVNAME=as5env

#Create and Activate environment
python3 -m venv $VENVNAME
source $VENVNAME/bin/activate

pip install --upgrade pip
pip install pandas
pip install matplotlib
pip install spacy
pip install opencv-python
pip install spacytextblob
pip install pyLDAvis
pip install seaborn
pip install gensim
python -m spacy download en_core_web_sm

# problems when installing from requirements.txt
test -f requirements.txt && pip install -r requirements.txt

#navigate to data folder and unzip
cd data 
unzip r_wallstreetbets.csv.zip
cd ..

#navigate to src folder
cd src

#run script
python LDA_model_reddit.py  

#deactivate environment
deactivate
