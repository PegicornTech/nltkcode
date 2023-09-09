import nltk
import pickle
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize

# Sample training data (you can replace this with your own data)
training_data = [
    ("This is a positive sentence.", "positive"),
    ("This is a negative sentence.", "negative"),
    # Add more training examples here
]

# Feature extraction function
def extract_features(text):
    words = word_tokenize(text)
    return dict([(word, True) for word in words])

# Create feature sets
feature_sets = [(extract_features(text), label) for (text, label) in training_data]

# Train a Naive Bayes classifier
classifier = NaiveBayesClassifier.train(feature_sets)

# Save the classifier to a pickle file
with open("classifier.pkl", "wb") as f:
    pickle.dump(classifier, f)

# Later, you can load the classifier from the pickle file
with open("classifier.pkl", "rb") as f:
    loaded_classifier = pickle.load(f)

# Test the loaded classifier
test_sentence = "This is a test sentence."
test_features = extract_features(test_sentence)
classification = loaded_classifier.classify(test_features)
print("Classification:", classification)


