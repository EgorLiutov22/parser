from nltk import word_tokenize, FreqDist
import pandas as pd

text = ' '
with open(r'E:\PycharmProjects\parser\res.csv') as f:
    for line in f:
        text += f.readlines()
    fdist = FreqDist(word.lower() for word in word_tokenize(text) if word.isalpha())
    df = pd.Series(fdist).reset_index(name="freq").rename(columns={"index": "word"})
print(df)
