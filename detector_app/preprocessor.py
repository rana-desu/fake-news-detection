"""
preprocessing the text:
    1. remove stop-words (is, and, the, etc.)
    2. lemmatization (reduce words to root form, running -> run)
    3. convert words to lowercase
    4. remove periods and other irrelevant special characters
    5. tokenization: split text into words
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")

# takes too fucking long, improve this
def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    # tokenization.
    words = text.split()
    # an array of words which excludes stopwords contained in stopword array.
    words = [word for word in words if word not in stopwords.words("english")]

    # stemming algorithm to reduce words to their root forms.
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return " ".join(words)
    