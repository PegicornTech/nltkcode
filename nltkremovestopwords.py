import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK's stop words dataset (if not already downloaded)
nltk.download("stopwords")
nltk.download("punkt")

def remove_stop_words(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Get the list of English stop words
    stop_words = set(stopwords.words("english"))

    # Remove stop words from the list of words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    return " ".join(filtered_words)

if __name__ == "__main__":
    input_text = "NLTK is a leading platform for building Python programs to work with human language data."

    filtered_text = remove_stop_words(input_text)
    print("Original text:")
    print(input_text)
    print("\nText after removing stop words:")
    print(filtered_text)

