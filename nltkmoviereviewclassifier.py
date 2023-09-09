#!/usr/bin/python
import nltk
import random
from nltk.corpus import movie_reviews
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download stopwords if not already available
nltk.download("stopwords")

# Create a list of stopwords to remove from reviews
stop_words = set(stopwords.words("english"))

# Create a list of documents, each containing a review and its label ("pos" or "neg")
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents to ensure randomness
random.shuffle(documents)

# Define a function to preprocess text
def preprocess_text(text):
    words = [word.lower() for word in text if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    return FreqDist(words)

# Extract features from reviews using the bag-of-words model
featuresets = [(preprocess_text(review), category) for (review, category) in documents]

# Split the data into a training set and a testing set
split_ratio = int(len(featuresets) * 0.8)
train_set, test_set = featuresets[:split_ratio], featuresets[split_ratio:]

# Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the classifier's accuracy on the testing set
accuracy = classify.accuracy(classifier, test_set)
print("Classifier Accuracy:", accuracy)

# Classify new reviews
new_review = "This movie is great!"
new_features = preprocess_text(word_tokenize(new_review))
classification = classifier.classify(new_features)
print("Classification of New Review:", classification)

