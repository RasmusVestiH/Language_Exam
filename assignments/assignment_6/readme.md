# Assignment 6: Deep Learning and Logistic Regression with Game of Thrones

## Description

This assignment was done in the group of Christoffer Kramer, Emil Buus Thomsen, Johanne Brandhøj Würtz and Rasmus Vesti Hansen.
For this assignment we worked with a dataset of Game of Thrones, where we were to apply logistic regression and deep learning models to quotes and make these machine learning tools try to compute what season of the show the dialogue was from. 

The results for this assignment turned out to be a bit short, as the best returned result was 33% on season 2 in the logistic regression model. For this we created a cross validation that has been commented out, but left in the script called "logistic_regression.py" in the src folder as it takes a long time to run. It is interesting how our deep learning model struggled a lot to find relations between dialogue and seasons of the show as the we only saw 27% accuracy on season 1. In the output the results can be seen and it is worth noting that 0 is season 1, 1 is season 2 etc. 
Christoffer managed to create some better accuracy as he set the source of input to the characters of the show instead of the dialogues. However I am not sure he has included this assignment in his portfolio. 


## Running it
For this assignment one can git clone this repository and run the bash script: "run_script" and the virtual environment will be created and the script will run and save the structure and results of the deep learning script and the logistic regression model. 