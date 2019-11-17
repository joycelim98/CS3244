# Clickbait Detection using Machine Learning

## Input Instances
The CSV file to be used to create the input instance dataframes can be found [here](https://github.com/sanjukta99/CS3244Project/blob/master/extracted_features.csv)

### Description of each column of *extracted_features.csv*
1. **instance** - Serial number of each instance. 
2. **total_tokens_title** - Total number of tokens (words + grammatical signs like !, ?, etc.) in the article's title
3. **total_tokens_content** - Total number of tokens (words + grammatical signs like !, ?, etc.) in the article's content
4. **total_words_title** - Total number of words in the article's title
5. **total_words_content** - Total number of words in the article's content
6. **total_filtered_words_title** - Total number of words in the article's title after removing the stopwords (you can find the list of stopwords that are excluded [here](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/))
7. **total_filtered_words_content** - Total number of words in the article's title after removing the stopwords (you can find the list of stopwords that are excluded [here](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/))
8. **count_exclamations_title** - Total number of exclamation marks in the article's title
9. **proportion_exclamations_title** - Proportion of total number of exclamation marks to the total number of tokens in the article's title
10. **count_exclamations_content** - Total number of exclamation marks in the article's content
11. **proportion_exclamations_content** - Proportion of total number of exclamation marks to the total number of tokens in the article's content
12. **count_question_title** - Total number of question marks in the article's title
13. **proportion_question_title** - Proportion of total number of question marks to the total number of tokens in the article's title
14. **count_question_content** - Total number of question marks in the article's content
15. **proportion_question_content** - Proportion of total number of question marks to the total number of tokens in the article's content
16. **count_allcaps_title** - Total number of words in allcaps in the article's title
17. **proportion_allcaps_title** - Proportion of allcaps words to the total number of words in the article's title
18. **count_allcaps_content** - Total number of words in allcaps in the article's content
19. **proportion_allcaps_content** - Proportion of allcaps words to the total number of words in the article's content
20. **count_contractions_title** - Total number of contractions in the article's title
21. **proportion_contractions_title** - Proportion of contractions to the total number of words after splitting on whitespace in the article's title
22. **count_contractions_content** - Total number of contractions in the article's content
23. **proportion_contractions_content** -  Proportion of contractions to the total number of words after splitting on whitespace in the article's content
24. **count_words_in_title_in_content** - Total number of times the filtered_words_title appear in the article's content. Duplicates have been handled
25. **proportion_words_in_title_in_content** - count_words_in_title_in_content divided by the total number of words in the content
26. **sentiment_title** - using TextBlob's sentiment function to determine the polarity of the article's title
27. **starts_with_number_title** - Whether or not the title starts with a number
28. **starts_with_number_content** - Whether or not the content starts with a number (i.e. first token is a number)
29. **len_longest_word_content** - Length of the longest word in the content, excluding (most) urls
30. **starts_with_5W1H_content** - Whether or not the content starts with one of the 5W1H
31. **starts_with_5W1H_title** - Whether or not the title starts with one of the 5W1H
32. **number_of_proper_nouns_in_content** - Total number of proper nouns that appear in the article's content. 
33. **proportion_number_proper_nouns_in_content** - number_of_proper_nouns_in_content divided by the total number of words in the content
,

## Acknowledgements
[Preprocessing of contractions and content of contractions.py](https://medium.com/@pemagrg/pre-processing-text-in-python-ad13ea544dae)
