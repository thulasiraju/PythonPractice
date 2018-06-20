from collections import Counter
import csv
import pandas as pd

all_words = []
count = []

def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())


words = dict(word_count('Commentary.csv'))
for key, value in words.items():
    temp1 = key
    temp3 = value
    all_words.append(temp1)
    count.append(value)

pd_def = pd.DataFrame({'Words': all_words, 'Count': count})
print(pd_def.info())
pd_def.to_csv('WordCount.csv')
