# NLP
##Introduction
A complete exploration of Natural language processing 
with python. The aim of this repository is to start with
the basics and move through more advanced code step by 
step.

##Basics
Using the nltk package, an analysis can be begun. This 
imports a series of texts on which functions from nltk
can be performed. In this way the basics can be 
established.

```python
>>> from nltk.book import *

*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
```

###Conducting text searches
To search on words exact to a text string use the method
.concordance for example

```python
text1.concordance("monstrous")
```

***What is the type of text1, from type(text1) we get
nltk.text.Text but what does that really mean. Dig deeper
into the class documentation of ntlk to find out.

###Conducting similar text searches

What about similes in the context of the text excerpts. 
 This is quite simple and powerful. On entering the 
 following into the command line a list of words are 
 returned which are similes in the authors context of 
 the word "monstrous"
 
 ```python
>>> text1.similar("monstrous")
determined fearless contemptible uncommon trustworthy doleful passing
singular untoward horrible christian mystifying imperial wise loving
lamentable exasperate mean lazy subtly
 ```
 
 On conducting the same analysis of text 2 we get the
 following
 ```python
 >>> text2.similar("monstrous")
 very heartily exceedingly so good a sweet extremely amazingly as vast
remarkably great
 ```
 
 On comparison of the two texts it can be seen that the
 context of the word monstrous takes on two different 
 meanings to the authors.
 
###Common Contexts

Find the contexts in which a list of words can appear.
Returns a frequency distribution mapping each context to
the amount of times that it was used. 

```python
text1.common_contexts(['murder', 'tell'])
will_thee and_him to_us i_you
```

###Dispersion Plot

A dispersion plot can demonstrate the occurrence of 
particular word usage in a text. For example in the 
artificial text example text4 which contains all 
inaugural speeches for the last 220 years we can 
see the distribution of certain words over the 
'length' of the text. The lexical dispersion plot 
works with matplotlib and numpy libraries imported.
 
```python
>>>text4.dispersion_plot(["citizens", 
"democracy", "freedom", "duties", "America",
"liberty","constitution"])
```
 
In this example the lexical dispersion plot demonstrates
that the words 'citizens', 'dutes' and 'liberty' have
been uniformly mentioned in the inaugural speech for 
the last 220 years. Whereas words like 'democracy' 
and 'America' have only been relatively recently 
included. Interestingly enough, while freedom has
always been mentioned it has become more fequent in 
recent times.

###Vocabulary of Text

The vocabulary of the text is the set of words which
it is comprised of. This can be expressed mathematically
as a sorted set with

```python
>>> sorted(set(text))
```

The lexical diversity of the text can be expressed as a
percentage with the function
 
```python
def percentage_words_to_text_length(text):
    return len(set(text))/len(text)*100
```

##Computing with Language

This section covers how to bring computational resources
to large quantities of text. Specifically around:

* What makes text distinct?
* Automatic methods to find characteristic words and 
expressions within a text

###Frequency Distribution

NLTK provides a function for the frequency distribution
with FreqDist(text) e.g. when plotting the distribution 
of tokens across words contained in the Jane Austin's 
Sense and Sensibility we obtain
 
 ```python
 fdist_ss = FreqDist(text2)
 fdist_ss.most_common(50)
 fdist_ss.plot(50, cumulative=True)
 ```
 
The cumulative distribution gives details about the
tokens that take up a significant portion of the text. 
In the case of Sense and Sensibility which contains 
a total of 141,576 words the 50 most common account for
approximately 70,000 which is roughly 50%. With the 
exception of Elinor and Marriane the remaining 48 words
are plumbing. We can conclude that Elinor and Marianne are
the protagonists in this text.

If the most frequent words do not aide the analysis of the
text then the 'hapaxes' or words that only occur once. To
get an understanding of the hapaxes use the following
  
```python
text.hapexes()
```

###Subsets of text with specific properties

If the most freqent or hapexes searches do not reveal
anything about the underlying context of the text then
searching for text subsets with specific properties
may help. Python provides the underlying set structure
to search against a property with list comprehension.

* [w for w in V if P(v)]
  
That is V is the set of vocabulary, w is a word element
and P(v) is a function mapping to the vocabulary. 

For example searching for long words in a text

```python
long_words = [w for w in set(text) if len(w)>15]
```

Searches can also be conducted on multiple function inputs, 
for example 

```python
relevant_long = [w for w in set(text) if len(w)>7 & fdist1[w]>7]
```

In fact the conditionals can be generalised even further with the following. Noticing that the conditional is always a function
we can write the search itself as a function that takes an anonymous function. 

```python
def search(fn, V):
    return [w for w in V if fn(w)]

>>> search(lambda a: len(a)>15, text)
>>> search(lambda a: len(a)>15 & fdist_ss[a]>7, text)
```

This saves a bit of code writing out the list comprehension for each of the searches and promotes a syntax that represents the
set notation. 

###Collocations and Bigrams

A collacation is a sequence of words that occur frequently
and often. 

To describe the usefulness of a collocation, first a 
description of a n-gram where n=2 is needed. This is 
known as a bigram. A bigram is a sequence of two adjacent
elements from a string of tokens, which are typically
letters, syllables or words. 

Bigrams help provide the conditional probability of a 
token given the preceding token.

math

The probability P() of a token W_n given the preceding 
token W_n-1 is equal to the joint probability of the 
sequence occurring divided by the probability of the 
preceding token occurring. 
 
An example of this can be constructed using the NLTK
method bigram()
 
 ```python
 list(nltk.bigram(['more','is','said','than','done']))
 ```
To get the collocations from a text 
 
 ```python
 >>>text.collocation()
 Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab; sperm
whale; Right Whale; Captain Peleg; New Bedford; Cape Horn; cried Ahab;
years ago; lower jaw; never mind; Father Mapple; cried Stubb; chief
mate; white whale; ivory leg; one hand
 ```
Thus one can get a real sense of the prose.

###Conditionals

The typical string methods can be applied to search for specific text constructs. 

| Method | Description |
|---|:---:|
|s.startswith(t)|string starts with t
|s.endswith(t)|string ends with t
|t in s| t is in the array s
|s.islower()| all lowercase
|s.isupper()| all upper case
|s.isalpha()| non empty alphabetical
|s.isalnum()| non empty alphanumeric
|s.isdigit()| non empty digits
|s.istitle()| initial captial letter sequence

An example

```python
search(lambda a: a.endswith('ble') & a.startswith('un'), text)
```

###Text Corpora

A quick interlude into text corpora is needed. Using the NLTK class is convenient and 
practical as we are effectively inheriting a set of powerful methods built for dealing with the text interpretation problem.
If anlaysis is being constructed quickly and a datasource is needed for testing then the NLTK package includes this via text
corpora. There are a large amount of corpora included but in this instance a demonstration of the Brown corpus is used. The brown
corpus includes multiple texts of varying genres and is ideal for use in anlaysis syntactic differences. More information is 
available from http://icame.uib.no/brown/bcm-los.html

```python
from nltk.corpus import brown
``` 

To construct a corpus from a directory of text files

```python
from ntlk.corpus import PlaintextCorpusReader
directory_address = .../files
words = PlaintextCorpusReader(directory_address, '.*')
words.fileids()
```

###Conditional Frequency Distributions Accessing Text Corpora Examples 

In this section, the above sections will be tied together to build some computations on text examples which are slightly
more involved.
 
Depending on the context of the conditional search, a conditional frequency distribution may be impractical if the
full set of words are included. Sometimes it may be more convenient and revealing to just take a subset. However, this
presents some problems when illusting the frequency distribution with a plot. Therefore two methods can be applied 
depending on whether a subset is being taken or the complete set. 


An example of the complete set is:

```python
cfd = nltk.ConditionalFreqDist((g,w) for g in ['adventure', 'fiction'] for w in brown.words(categories=g))
cfd.plot()
```

Which is messy and does not reveal a great deal about the texts. 

```python
import operator
d = {'adventure': [x for x,_ in nltk.FreqDist(brown.words(categories='adventure')).most_common(50)], 
     'fiction': [x for x,_ in nltk.FreqDist(brown.words(categories='fiction')).most_common(50)]}

genre_words = [(g,w) for g in ['adventure', 'fiction'] for w in brown.words(categories=g) if w in d[g]]

cfd = nltk.ConditionalFreqDist(genre_words)
cdf.sort(key=operator.itemgetter(1))
cfd.plot(cumulative=True)
``` 

To conduct further anlysis and plotting that can be saved to the image processor we can send the data from the 
conditional frequency distribution to a pandas dataframe. At this point it is useful to understand exactly what the 
conditional frequency distribution is. With
```python
>>>type(cfd)
nltk.probability.ConditionalFreqDist
>>>nltk.probability.ConditionalFreqDist.__doc__
    The frequency distribution for each condition is accessed using
    the indexing operator:

        >>> cfdist[3]
        FreqDist({'the': 3, 'dog': 2, 'not': 1})
        >>> cfdist[3].freq('the')
        0.5
        >>> cfdist[3]['dog']
        2

    When the indexing operator is used to access the frequency
    distribution for a condition that has not been accessed before,
    ``ConditionalFreqDist`` creates a new empty FreqDist for that
```
When looking through the documentation there is more useful information on what the CFD is, however, we are only
interested in how to access it. 
```python
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
```

For more information on NLTK plot
```python
cfd.plot.__doc__
```
 
 
 
