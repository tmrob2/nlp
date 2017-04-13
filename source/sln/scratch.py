import nltk
import pandas as pd
from nltk.book import *
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from bs4 import BeautifulSoup
from urllib import request
import praw


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


#Wordnet references

for syn in wn.synsets('dish'):
    print(syn, syn.lemma_names())

types_of_dish = wn.synset('dish.n.01').hyponyms()

##############################################################################
#                                CHAPTER 3
##############################################################################
#BeautifulSoup
#input a url
url = 'https://www.reddit.com/r/news/'
html = request.urlopen(url).read().decode('utf8')
html[:60]
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
print(tokens)

def return_client_id():
    return "O_zXN9Bh5bl58Q"
    
def return_client_secret():
    return "NHa0eYhJ5ZQoPpSHVGK2xSiFGPY"
    
def user_agent():
    return "test by /u/ligitimate_human"

def define_reddit(password, username):
    reddit = praw.Reddit(client_id=return_client_id(),
                     client_secret=return_client_secret(),
                     password = password,
                     user_agent=user_agent(),
                     username = username)
    return reddit

url = "http://www.politico.com/story/2017/04/nunes-to-step-aside-from-russia-probe-236951?cmpid=sf"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html).get_text()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens) 

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')

f = open(path, encoding='latin2')

for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
    
import unicodedata

lines = open(path, encoding='latin2').readlines()
line = lines[2]
print(line.encode('unicode_escape'))

for c in line:
    if ord(c) >127:
        print('{} U+{:04x} {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
            
#Using basic meta characters

#searching for words ending in ed
[w for w in wordlist if re.search('ed$', w)]
 
#Wild cards 8 letter word with js in the 3rd and t in the 6th positions 
[w for w in wordlist if re.search('^..j..t..$', w)]
 
#If the ^ or the $ are left out then this will not constrain the word length
#i.e. the words could be any set of words with length +..j..t..+

chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))

[w for w in chat_words if re.search('^m+i+n+e+$', w)]
 
[w for w in chat_words if re.search('^[ha]+$', w)]
 
 wsj = sorted(set(nltk.corpus.treebank.words()))
 
 fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
 
 fd.most_common(12)
 
##############################################################################
#                              chapter 4
##############################################################################

from numpy import arange
from matplotlib import pyplot as plt
import nltk

colours = 'rgbcmyk'

def bar_chart(categories, words, counts, colours, title='Example'):
    "count of words by category represented as a bar chart"
    
    ind = arange(len(words))
    width = 1/(len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = plt.bar(ind+c*width, counts[categories[c]], width,
                       color = colours[c%len(colours)])
        bar_groups.append(bars)
        
    plt.xticks(ind+width, words)
    plt.legend([b[0] for b in bar_groups], categories, loc = 'upper left')
    plt.ylabel('Frequency')
    plt.title(title)

genres = ['news','religion','hobbies','government', 'adventure']
modals = ['can', 'could','may','might','must','will']

cfdist = nltk.ConditionalFreqDist((genre, word) for genre in genres
                                  for word in nltk.corpus.brown.words(categories = genre)
                                  if word in modals)
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]

bar_chart(genres, modals, counts, colours, 'modals and their fequency distributions')

import networkx as nx
import matplotlib
from networkx.drawing.nx_agraph import graphviz_layout

from nltk.corpus import wordnet as wn
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 10,6

def traverse(graph, start, node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name, child.name)
        traverse(graph, start, child)
        
def hyponym_graph(start):
    G = nx.Graph()
    G.depth = {}
    traverse(G, start, start)
    return G
    
def graph_draw(graph):
    pos = nx.fruchterman_reingold_layout(graph)
    
    nx.draw_networkx_nodes(graph, pos,
                           node_size = [16*graph.degree(n) for n in graph],
                           node_color = [graph.depth[n] for n in graph],
                           alpha = 0.4)
    nx.draw_networkx_edges(graph, pos, alpha = 0.4, node_size = 0, width = 1,
                           edge_color = 'm')

    matplotlib.pyplot.show()

dog = wn.synset('dog.n.01')
graph = hyponym_graph(dog)
graph_draw(graph)

