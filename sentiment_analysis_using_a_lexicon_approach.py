# -*- coding: utf-8 -*-
"""sentiment analysis using a lexicon approach.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jXtj_cLPlC9oAm85wR-1cpd9ERtf-iHq
"""

# Python source code for sentiment analysis using a lexicon approach with dictionary datasets for training

import csv
import pandas as pd

def load_lexicon(file_path):
    lexicon = {}
    with open(file_path, 'r') as lexicon_file:
        reader = csv.reader(lexicon_file)
        for row in reader:
            word = row[0]
            sentiment = row[1]
            lexicon[word] = sentiment
    return lexicon

def analyze_sentiment(text, lexicon):
    words = text.lower().split()
    sentiment_scores = []
    for word in words:
        if word in lexicon:
            sentiment_scores.append(int(lexicon[word]))
    if sentiment_scores:
        sentiment_score = sum(sentiment_scores) / len(sentiment_scores)
        if sentiment_score > 0:
            return 'positive'
        elif sentiment_score < 0:
            return 'negative'
    return 'neutral'

# Load the lexicon
lexicon = load_lexicon('sentiment_lexicon.csv')

# Load test data
with open('test_twwets.csv', 'r') as test_file:
        reader = csv.reader(test_file)
        data = [['tweet'],['Polarity']]
        for row in reader:
            MyPolarity = ' ';
            tweet = row[0]
            MyPolarity = analyze_sentiment(row[0], lexicon)
            data.append([row[0],MyPolarity])

#Create a DataFrame
annotatedtweets = pd.DataFrame(data, columns=['tweet','Polarity'])
annotatedtweets.to_csv('myannotatedtweets.csv')