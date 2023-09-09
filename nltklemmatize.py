#!/usr/bin/python
from nltk.stem import WordNetLemmatizer

# Create a WordNetLemmatizer object
lemmatizer = WordNetLemmatizer()

# Lemmatize words
words = ["running", "better", "mice"]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the lemmatized words
print(lemmatized_words)
