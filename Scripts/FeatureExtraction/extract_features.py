"""
template to begin feature extraction
"""
from small_dataset import get_small_dataset
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from textblob import TextBlob
from contractions import contractions_dict
import csv

data = [["instance", "total_tokens_title", "total_tokens_content", "total_words_title", "total_words_content"
, "total_filtered_words_title", "total_filtered_words_content", "count_exclamations_title", "proportion_exclamations_title"
, "count_exclamations_content", "proportion_exclamations_content", "count_question_title", "proportion_question_title"
, "count_question_content", "proportion_question_content", "count_allcaps_title", "proportion_allcaps_title", "count_allcaps_content"
, "proportion_allcaps_content", "count_contractions_title", "proportion_contractions_title", "count_contractions_content"
, "proportion_contractions_content", "count_words_in_title_in_content", "proportion_words_in_title_in_content"
, "sentiment_title"]]

stop_words = set(stopwords.words('english'))

df = get_small_dataset()
num_instances = df.shape[0]

for i in range(num_instances):
    instance = i + 1
    title = df.loc["{}".format(instance) ,"title"]
    content = df.loc["{}".format(instance) ,"content"]

    #Using TextBlob to tokenize into tokens and words
    blob_title = TextBlob(title)
    tokens_title = blob_title.tokens
    words_title = blob_title.words

    blob_content = TextBlob(content)
    tokens_content = blob_content.tokens
    words_content = blob_content.words

    #filtering the words to remove stop words
    filtered_words_title = {w for w in words_title if not w in stop_words}

    filtered_words_content = [w for w in words_content if not w in stop_words]

    #total number of tokens
    total_tokens_title = len(blob_title.tokens)
    total_tokens_content = len(blob_content.tokens)

    #total number of words
    total_words_title = len(words_title)
    total_words_content = len(words_content)

    #total number of words after filtering
    total_filtered_words_title = len(filtered_words_title)
    total_filtered_words_content = len(filtered_words_content)


    ### 
    # Proportion of Total number of exclamation marks to Total number of tokens, 
    # i.e. words + grammatical signs
    ###
    count_exclamations_title = tokens_title.count('!')
    proportion_exclamations_title = 0 if total_tokens_title == 0 else (count_exclamations_title/total_tokens_title)

    count_exclamations_content = tokens_content.count('!')
    proportion_exclamations_content = 0 if total_tokens_content == 0 else (count_exclamations_content/total_tokens_content)

    ### 
    # Proportion of Total number of question marks to Total number of tokens, 
    # i.e. words + grammatical signs
    ###
    count_question_title = tokens_title.count('?')
    proportion_question_title = 0 if total_tokens_title == 0 else (count_question_title/total_tokens_title)

    count_question_content = tokens_content.count('?')
    proportion_question_content = 0 if total_tokens_content == 0 else (count_question_content/total_tokens_content)

    ### 
    # Proportion of all caps words to Total number of tokens, 
    # i.e. words + grammatical signs
    ###
    count_allcaps_title = 0
    for token in words_title:
        if token.isupper():
            count_allcaps_title += 1
    proportion_allcaps_title = 0 if total_words_title == 0 else (count_allcaps_title/total_words_title)

    count_allcaps_content = 0
    for token in words_content:
        if token.isupper():
            count_allcaps_content += 1
    proportion_allcaps_content = 0 if total_words_content == 0 else (count_allcaps_content/total_words_content)
    
    ### 
    # Proportion of all contractions to total number of words, 
    # i.e. words + grammatical signs
    # contractions_dict was taken from https://github.com/pemagrg1/Text-Pre-Processing-in-Python/blob/master/individual_python_files/contractions.py
    ###
    count_contractions_title = 0
    for word in title.split():
        if word in contractions_dict:
            count_contractions_title += 1
    
    proportion_contractions_title = 0 if len(title.split()) == 0 else count_contractions_title/len(title.split())
    

    count_contractions_content = 0
    for word in content.split():
        if word in contractions_dict:
            count_contractions_content += 1

    proportion_contractions_content = 0 if len(content.split()) == 0 else count_contractions_content/len(content.split())

    ### 
    # Words from the title being repeated in the content
    # Take the title words list, remove stopwords and store in a dict
    # Keep track of words occuring in content and update count
    ###
    count_words_in_title_in_content = 0

    for word in filtered_words_content:
        if word in filtered_words_title:
            count_words_in_title_in_content += 1
    
    proportion_words_in_title_in_content = 0 if total_filtered_words_content == 0 else count_words_in_title_in_content/total_filtered_words_content

    ###
    # Sentiment analysis to get the polarity and subjectivity of the title
    ###
    sentiment_title = blob_title.sentiment[0]

    instance = [instance, total_tokens_title, total_tokens_content, total_words_title, total_words_content, total_filtered_words_title, total_filtered_words_content, count_exclamations_title, proportion_exclamations_title
    , count_exclamations_content, proportion_exclamations_content, count_question_title, proportion_question_title
    , count_question_content, proportion_question_content, count_allcaps_title, proportion_allcaps_title, count_allcaps_content
    , proportion_allcaps_content, count_contractions_title, proportion_contractions_title, count_contractions_content
    , proportion_contractions_content, count_words_in_title_in_content, proportion_words_in_title_in_content
    , sentiment_title]

    data.append(instance)

with open('extracted_features.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    for row in data:
        if row:
            writer.writerow(row)

csvFile.close()












    
            








    