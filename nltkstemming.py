#!/usr/bin/python
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

example_words = ["python","pythoner", "pythoning","pythonly"]

for w in example_words:
    print(ps.stem(w))
    
new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
