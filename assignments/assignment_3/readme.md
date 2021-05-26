# Assignment 3: Sentiment Analysis

## Description

For this assignment we worked with a dataset of 1 mio. headlines and the main purpose was to incorporate sentiment analytics for these headlines. 

I created a data_setup file that would create a sample called "data_scores" of the very large data so the process would be easier and faster. 
But before this could work a bash script ("run_script") was created in order for the process of reproducing the code was easy. This script also unzips the data so that it would be possible to upload it on github (size limit of 50Mb). 
After this the data_setup script will run and setting up the data so the actual sentiment_analysis would work and create the two models found in the output folder. 


The result: 
On the first run we sorted the headlines into weeks and here we saw that there is a radical negative sentiment in the middle of year 3 and 4, which would be 2006 and 2007, which could be around the financial crisis meaning news were more negative. Opposite can be said just before year 12 (2015) where there is a spike in positve sentiment.  

The second part of the sentiment was for months where we saw similar patterns to the weeks, but it is worth noting that the sentiment never goes to a negative point but instead only touches a neutral in between year 3 and 4. It also displays a positive spike at year 12 (2015).


## Running it

I have created a run_script.sh that will unzip the data and setup the data scores in a separate script in the src folder. Afterwards the actual sentiment_analysis script can run, which will save the models of the sentiment analysis of the headlines in the output folder. 