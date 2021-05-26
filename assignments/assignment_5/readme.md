# Assignment 5: LDA model of r/wallstreetbets

## Description

For this assignment I worked Christoffer Kramer, Johanne Brandhøj Würtz and Emil Buus Thomsen. 
We used the LDA utils package provided by Ross Deans Kristensen-McLachlan in the course Language Analytics.  
For this we wanted to examine an LDA models categorization of the subreddit Wallstreetbets as they discussed stock trading with their jargon and vocabulary. E.g. "to the moon" would mean they wanted the stocks to rise. This sort of language would be a interesting thing to create topics based on and see how they would be sorted. 
As we used a sample of 10.000 this also means the results will vary meaning some results end up strange while others seem to make some sense in this context. 


We expected "gme" to be an important word in the topics and in the output it is shown how one topic has this the most relevant and used word. This is the abbreviation of the Gamestop stock that was heavily discussed as it was shown how hedgefunds were betting against an increase in these stocks and thus creating an interest for ordinary people to invest in these stocks to increase its value. Along with this it is visible how "robinhood" (a stock trading platform), "stock" and "amc" (stock with the same hedgefund based conflict as "gme") was also set in the same topic. The other two topics were also sorted in some sort of category as one had "market", "stock" and "money" in relatively high places while words like "retard" and "tomorrow" also had prominent placements in this topic. This means that we still had some confusion and disruption in modelling of the topics. To clarify this in the context "retard" was used by the users to describe themselves after giving advice on the stocks to make fun of the hedgefunds in a sarcastic manner. Another topic had "moon" as the most dominant word and with a high relevancy meaning the LDA picked up some sort of interest in this word. However it can be discussed whether the context of this topic fits the actual usage on the subreddit.       


## Running it
For this assignment I have also made a bash script called "run_script" that will unzip the data and run the LDA model of this resulting in the LDA_board.html file will be saved in the output folder. 