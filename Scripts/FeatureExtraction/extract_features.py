"""
extract_features.py: extract relevant features for training, from small dataset
"""
from small_dataset import get_small_dataset
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# data is a pandas dataframe
df = get_small_dataset()
num_instances = df.shape[0]

# to store new data (extracted features)
data = {}

stop_words = set(stopwords.words('english'))
punct_noted = ['!', '?']

for i in range(num_instances):
    instance_id = df['id'][i]
    title = df['title'][i]
    content = df['content'][i]

    ### get frequencies of words in title appearing in content ##
    blob_title = TextBlob(title)
    title_words = blob_title.words.lower()
    result = [i for i in title_words if not i in stop_words]
    result = list(dict.fromkeys(result))    # remove duplicate words

    # iterate through content to find title words' frequencies
    blob_content = TextBlob(content)
    freqs = {}

    content_words_dict = blob_content.word_counts
    for word in result:
        word_count = content_words_dict[word]
        freqs[word] = word_count

    print(freqs)


    ### get number of exclamation marks or question marks in title ###
    title_tokens = blob_title.tokens
    title_punct_count = sum(1 for i in title_tokens if i in punct_noted)
    
    ### get number of exclamation marks or question marks in content #
    content_tokens = blob_content.tokens
    content_punct_count = sum(1 for i in content_tokens if i in punct_noted)

    ### detect number of words written in all-caps in title






