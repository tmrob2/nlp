import nltk
from nltk.book import *

def lexical_diversity(text):
    return len(set(text))/len(text)

def search(fn, V):
    return [w for w in V if fn(w)]

d = {'news': [x for x,_ in nltk.FreqDist(brown.words(categories='news')).most_common(50)], 
     'romance': [x for x,_ in nltk.FreqDist(brown.words(categories='romance')).most_common(50)]}

genre_words = [(g,w) for g in ['news', 'romance'] for w in brown.words(categories=g) if w in d[g]]

"""The charting is somewhat limited therefore we will want to do some modifications to make the charting richer"""

word = [k for (k,v) in cfd['news'].items()]


