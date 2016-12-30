import nltk
import pandas as pd
from nltk.book import *
import matplotlib.pyplot as plt

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
        words = [w for w,c in cfd[k].items()]
        value = [cfd[k][w] if w in words else 0 for w in ls]
        s = pd.Series(data=value, index=ls)
        df[k] = s

    return df

def set_of_words(cfd: nltk.probability.ConditionalFreqDist):
    S = set()
    for k in cfd.keys():
        word = [w for w,c in cfd[k].items()]
        S = S.union(set(word))
    ls = [i for i in S]
    return ls
