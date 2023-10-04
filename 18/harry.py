import collections
import os
import urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)

with open(harry_text, mode="r", encoding="utf-8") as file:
    harry = file.read().lower().split()

with open(stopwords_file, mode="r", encoding="utf-8") as file:
    stopwords = file.read().split()


def get_harry_most_common_word():
    cleaned_words = ["".join(filter(str.isalnum, word)) for word in harry]

    non_stopwords = [
        word for word in cleaned_words if word != "" and word not in stopwords
    ]

    return collections.Counter(non_stopwords).most_common(1)[0]


get_harry_most_common_word()
