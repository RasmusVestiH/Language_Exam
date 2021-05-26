# Assignment 7: Wine Descriptions (Self-assigned) 

## Description

For this assignment I wanted to create and LDA model on wine reviews to see how the topics would be sorted on a random sample of 20.000 out of the dataset of ~97k wine descriptions and what would be seen as relevant in this context. The dataset was downloaded from kaggle at https://www.kaggle.com/zynicide/wine-reviews
and I decided to just use the csv file and focus on the column with the description of the wine. 


The results in LDA model showed how the topics were related to the flavors and terms used for white- and red wine. With three topics the first described overall terms for the wine description such as the "flavor", "aroma", "fruit" and such while the second topic had flavors, notes and grapes related to white wine which was "acidity", "apple", "citrus", "pear", "honey" while grapes mentioned was "chardonnay" and "pinot". It's worth considering how pinot could be pinot gris or pinot noir, which is a red wine, however often with fruity notes and a light structure. The third is in contrast to the second more sorted on red wine and the notes one might find here and grapes such as "cabernet", "sauvignon", and "merlot" while the notes are more "blackberry", "oak" and "tannin" also being a strong word in this context. 
This means that the LDA model seems to have sorted the topics as one general, one white and one red wine sort of categorization. 

## Running it
This assignment has a bash script called "run_script" that will unzip the dataset and setup the data for the LDA model and run it all together. The results will be saved in the output folder. In the output folder there is an example of the LDA board of all the descriptions (97.000) but it takes a lot of time to load this, so I figured it would just be interesting to have as a reference in case one was to reproduce and change the sample size or such and see how the results could be altered. 