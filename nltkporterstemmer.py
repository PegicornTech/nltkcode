#!/usr/bin/python
import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')  # Download the NLTK data if you haven't already

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Sample text
text = "The quick brown foxes jumped over the lazy dogs. Jumps jumping jumped"

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Apply Porter Stemming to each word
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original words and their stemmed forms
for i in range(len(words)):
    print(f"Original: {words[i]}\tStemmed: {stemmed_words[i]}")
