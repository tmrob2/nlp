import nltk
import pandas as pd
from nltk.book import *
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

def lexical_diversity(text):
    return len(set(text))/len(text)

def cfd_to_dataframe(cfd: nltk.probability.ConditionalFreqDist):
    """
    This function takes an NLTK conditional frequency distribution and
    converts it to a pandas dataframe object. Limitations of the
    nltk.probability.ConditionFreqDist do not allow for extra analysis one might
    do with the data available.
    :param cfd: A conditional frequency Distribution is a dictionary of pairs i.e. genre : (word, count)
    :return: a pandas.DataFrame object with indexed to words with counts headed by their genre
    """
    df = pd.DataFrame()
    ls = set_of_words(cfd)
    # Could not think of a better way of getting around the double loop as we need to include
    # all of the words from all lists i.e. A = [a,b,c] B = [a,d,e] then we can't serialise the two with
    # with an index from one or the other it must be both.
    for k in cfd.keys():
        words = [w for w, c in cfd[k].items()]
        value = [cfd[k][w] if w in words else 0 for w in ls]
        s = pd.Series(data=value, index=ls)
        df[k] = s

    return df

def set_of_words(cfd: nltk.probability.ConditionalFreqDist):
    """
    This function takes the union of word sets in a conditional frequency distribution
    and returns an iterable list.
    :param cfd: conditional frequecy distribution
    :return: list of words A1 & A2 & ... & An
    """
    S = set()
    for k in cfd.keys():
        word = [w for w,c in cfd[k].items()]
        S = S.union(set(word))
    ls = [i for i in S]
    return ls

def generate_cfd(ls: list, corp: nltk.corpus.util.LazyCorpusLoader, freq: int=None):
    """
    A function which generates a conditional frequency distribution based on an input corpus
    and a list of categories contained within that corpus. Knowledge of the corpus is necessary
    to input the list. Corpora may be navigated with corp.fileids()
    :param ls: list of categories of type string
    :param corp: corpus
    :param freq: lower bound of the most frequent items e.g. 50 most common
    :return: a conditional frequency distribution
    """
    d = {}
    for i in ls:
        d[i] = [x for x,_ in nltk.FreqDist(corp.words(categories=i)).most_common(freq)]
    genre_words = [(g, w) for g in ls for w in corp.words(categories=g) if w in d[g]]
    cfd = nltk.ConditionalFreqDist(genre_words)
    return cfd

# Lexical References: Wordlist corpora in nltk

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

def remove_stops(text):
    stops = stopwords.words('english')
    non_stop = [w for w in text if w.lower() not in stops and w.isalpha()]
    return non_stop

def content_fraction(text):
    stops = stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

def names_in_text(text):
    male_names = nltk.corpus.names.words('male.txt')
    female_names = nltk.corpus.names.words('female.txt')
    text_names = [w for w in text if w in male_names or w in female_names]
    return text_names






