#!/usr/bin/python

import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr Smith, how are you today? I'm looking for my cat. How is your wife? The car is red."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
