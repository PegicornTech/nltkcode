#!/usr/bin/python
import nltk
import random
from nltk.corpus import reuters
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

# Download stopwords if not already available
nltk.download("stopwords")

# Create a list of stopwords to remove from articles
stop_words = set(stopwords.words("english"))

# Create a list of documents, each containing an article and its category
documents = [(list(reuters.words(fileid)), category)
             for category in reuters.categories()
             for fileid in reuters.fileids(category)]

# Shuffle the documents to ensure randomness
random.shuffle(documents)

# Define a function to preprocess text
def preprocess_text(text):
    words = [word.lower() for word in text if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    return FreqDist(words)

# Extract features from articles using the bag-of-words model
featuresets = [(preprocess_text(article), category) for (article, category) in documents]

# Split the data into a training set and a testing set
train_set, test_set = train_test_split(featuresets, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the classifier's accuracy on the testing set
accuracy = classify.accuracy(classifier, test_set)
print("Classifier Accuracy:", accuracy)

# Classify new articles
new_article = "Apple announces the launch of a new iPhone model."
new_features = preprocess_text(word_tokenize(new_article))
classification = classifier.classify(new_features)
print("Classification of New Article:", classification)

