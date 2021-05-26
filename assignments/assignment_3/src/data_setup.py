#---------The script for the sentiment data:-------
#This is primary code for creating the sentiment scores, but this proces takes over 15 mins so for it to be easier I will include
# the csv file this code creates instead, which can be loaded below this code. 

#Libraries
import os
import spacy
import sys
sys.path.append(os.path.join(".."))
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from spacytextblob.spacytextblob import SpacyTextBlob
#initialise spacy
nlp = spacy.load("en_core_web_sm")

def main():
    #Creating a container for the sentiment scores:
    output = []

    #The loop runs through the headlines in the csv-file.
    news_data = os.path.join("..","data", "abcnews-date-text.csv") #First we load in the dataset
    data = pd.read_csv(news_data) #defining it and reading the csv
    
    #Adding spaCyTextBlob to spaCy pipeline: 
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    
    for doc in nlp.pipe(data["headline_text"], batch_size = 5000,
                   disable=["tagger", "parser", "ner"]):
        #Disabling to make the code run faster, since there is a lot of data and the processing time is long.
        output.append(doc._.sentiment.polarity) #appending the scores to our output container.

    # Creating a new dataframe
    data_df = pd.DataFrame(data)

    # Appending a new series/column to the new df, with the scores
    data_df["scores"] = output
    data_df.to_csv("../data/data_scores") #Here we wrote the dataframe to the csv
    
if __name__ == "__main__":
    main()