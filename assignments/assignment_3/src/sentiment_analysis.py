#-------------------------------Import the libraries--------------------------------------
import os
import sys
import spacy
from pathlib import Path
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.pyplot import figure
from spacytextblob.spacytextblob import SpacyTextBlob
#initialise spacy
#import en_core_web_sm
nlp = spacy.load("en_core_web_sm")

#--------------------------------The main script-------------------------------------------
def main():
    news_data = os.path.join("..","data", "abcnews-date-text.csv") #First we load in the dataset
    data = pd.read_csv(news_data) #defining it and reading the csv
    
    #Adding spaCyTextBlob to spaCy pipeline: 
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    
    data_df_path = os.path.join("../data/data_scores") #I made a data_scores file to save time instead of the data_setup
    data_df = pd.read_csv(data_df_path) # with this the data 
    daily_avg_sentiment = data_df.groupby("publish_date").mean() #Here we group the data_df by the date of publish. 
    
    #To make the figures we create a mean_scores list in which we loop the scores and append on index
    mean_scores = []
    for i in daily_avg_sentiment ["scores"]:
        mean_scores.append(i)

        
#---------------------------------Plotting the sentiment scores------------------------------
    #First we create the weekly averages with the pandas series function
    smoothed_sentiment_weeks = pd.Series(mean_scores).rolling(7).mean()

    #Create figure
    fig = plt.figure(figsize = (15,10))
    #Create a grid for readability
    plt.grid()
    #Plot average sentiment for 7 days rolling
    plt.plot(smoothed_sentiment_weeks)
    #Create title, labels and legend
    plt.title("Headline sentiment since 2003",fontsize= 20)
    plt.xlabel("Years since 2003", fontsize= 15, labelpad=10)
    plt.ylabel("Sentiment Score", fontsize= 15)
    plt.legend(["Weekly rolling average"],
               loc='upper right',
               fontsize= 12)
    #Set x ticks to be in years rather than days, this meaning the plot shows years (0 being 2003 and 18 being 2021) 
    plt.xticks(np.arange(0, len(mean_scores)+1,365), range(0,18))
    #Save the figure in output
    plt.savefig('../output/weekly_model.png')
    
    #Same process as above for the monthly but 30 as the rolling key instead of 7
    smoothed_sentiment_months = pd.Series(mean_scores).rolling(30).mean()

    #Create figure
    fig = plt.figure(figsize = (15,10)) 
    #Create a grid for readability
    plt.grid()
    #Plot average sentiment for 30 days rolling
    plt.plot(smoothed_sentiment_months)
    
    #Create title, labels and legend
    plt.title("Headline sentiment since 2003",fontsize= 20)
    plt.xlabel("Years since 2003", fontsize= 15, labelpad=10)
    plt.ylabel("Sentiment Score", fontsize= 15)
    plt.legend(["Monthly rolling average"],
               loc='upper right',
               fontsize= 12)

    #Set x ticks to be in years again. 
    plt.xticks(np.arange(0, len(mean_scores)+1,365), range(0,18))
    #Save the figure in output
    plt.savefig('../output/monthly_model.png')
if __name__ == "__main__":
    main()