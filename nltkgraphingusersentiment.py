#!/usr/bin/python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download the VADER lexicon (if not already downloaded)
nltk.download("vader_lexicon")

# Create a list of movie reviews
movie_reviews = [
    "This movie is fantastic! I was thrilled from start to finish.",
    "The acting was terrible, and the plot made no sense.",
    "I loved the cinematography, but the story was weak.",
    "It was a masterpiece, truly brilliant in every way.",
    "The dialogue was cringe-worthy, and I couldn't wait for it to end.",
]

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment for each movie review
sentiments = []
for review in movie_reviews:
    sentiment_scores = sia.polarity_scores(review)
    sentiments.append(sentiment_scores["compound"])

# Define labels for the reviews
labels = ["Review 1", "Review 2", "Review 3", "Review 4", "Review 5"]

# Create a bar graph to visualize sentiment
plt.figure(figsize=(10, 5))
plt.bar(labels, sentiments, color=['green' if s > 0 else 'red' for s in sentiments])
plt.title("Sentiment Analysis of Movie Reviews")
plt.xlabel("Movie Review")
plt.ylabel("Sentiment Score (Compound)")
plt.ylim(-1, 1)  # Set the y-axis limits to -1 and 1
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.show()

