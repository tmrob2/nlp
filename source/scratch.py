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
    for k in cfd.keys():
        word = [k for k,v in cfd[k].items()]
        value = [v for k,v in cfd[k].items()]
        s = pd.Series(data=value, index=word)
        df[k] = s

    return df
