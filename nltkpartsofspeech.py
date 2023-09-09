#!/bin.python

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Print the words and their corresponding POS tags
for word, pos_tag in pos_tags:
    print(f"Word: {word}\tPOS Tag: {pos_tag}")
