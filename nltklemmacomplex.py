#!/usr/bin/python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download NLTK data if you haven't already
nltk.download('punkt')
nltk.download('wordnet')

# Create a WordNetLemmatizer object
lemmatizer = WordNetLemmatizer()

# Define a function to get the WordNet POS tag from Penn Treebank POS tags
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun

# Tokenize a sentence
sentence = "The quick brown foxes are jumping over the lazy dogs"
tokens = word_tokenize(sentence)

# Part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)

# Lemmatize words based on their POS tags
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]

# Print the lemmatized words
print(lemmatized_words)
