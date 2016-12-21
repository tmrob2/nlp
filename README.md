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


 
 
 
 
