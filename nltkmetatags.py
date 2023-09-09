#!/usr/bin/python

import argparse
from nltk.tokenize import word_tokenize

def main():
    parser = argparse.ArgumentParser(description="Process and create HTML keywords meta tag")
    parser.add_argument("--input-file", required=True, help="Path to the input text file")
    parser.add_argument("--output-file", required=True, help="Path to the output HTML file")
    args = parser.parse_args()

    with open(args.input_file, "r") as input_file:
        text = input_file.read()

    words = word_tokenize(text)
    cleaned_words = [word for word in words if word.isalnum()]

    sorted_unique_words = sorted(set(cleaned_words))

    with open(args.output_file, "w") as output_file:
        output_file.write("<html>\n<head>\n")
        output_file.write("<meta name=\"keywords\" content=\"")
        output_file.write(", ".join(sorted_unique_words))
        output_file.write("\">\n</head>\n<body>\n</body>\n</html>")

if __name__ == "__main__":
    main()

