#!/usr/bin/env bash

#Environment name
VENVNAME=as7env

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

cd data 
unzip winemag-data_first150k.csv.zip
cd ..


# problems when installing from requirements.txt
test -f requirements.txt && pip install -r requirements.txt

#navigate to src folder
cd src

#run script
python wine_description.py  


#deactivate environment
deactivate
