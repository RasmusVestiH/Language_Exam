''' --Assignment 1-- '''
'''
Basic scripting with Python
 
Using the corpus called 100-english-novels found on the cds-language GitHub repo, write a Python programme which does the following:
 
Calculate the total word count for each novel
Calculate the total number of unique words for each novel
Save result as a single file consisting of three columns: filename, total_words, unique_words
 
 
General instructions

For this exercise, you can upload either a standalone script OR a Jupyter Notebook
Save your script as word_counts.py OR word_counts.ipynb
You can either upload the script/notebook here or push to GitHub and include a link - or both!
Your code should be clearly documented in a way that allows others to easily follow the structure of your script.
Similarly, remember to use descriptive variable names! A name like word_count is more readable than wcnt.


Purpose

This assignment is designed to test that you have a understanding of:
 
how to structure, document, and share a Python script;
how to effectively make use of native Python data structures, functions, and flow control;
how to load, save, and process text files.
'''

#-----------------Script------------------

# To start of we need to import the 100-english-novels in the data folder.
import os
import pandas as pd
from pathlib import Path


def main():
    # Set the directory of the files
    data_path = os.path.join("..", "data", "100_english_novels", "corpus")
    # Use pandas to create a dataframe with useful columns
    table = pd.DataFrame(columns = ["filename", "word_count", "unique_words"])
    
    #Here we have a loop that checks if the textfiles are present and correct.
    for filename in Path(data_path).glob("*.txt"): 
        with open(filename, "r", encoding="utf-8") as file: 
            # We save the text as we read the files
            loaded_text = file.read()
            # Count the words by splitting the text 
            word_count = loaded_text.split()
            # Count the unique words with the "set" function
            unique_words = set(word_count)
            # Make the count based on the lengths of the unique_words
            unique_count = len(unique_words)
            # Create a temporary dataframe with the columns above
            temp_df = ({'filename': filename, 'word_count': len(word_count), 'unique_words': unique_count})
            # appending the temporary dataframe to the dataframe "table"
            table = table.append(temp_df, ignore_index=True)

# When saving the output we create an outpath and use the pandas function to_csv to save it as a csv file
    outpath = os.path.join("..","output","wordcount.csv")
    table.to_csv(outpath)
        


if __name__ == "__main__":
    main()