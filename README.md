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
 
 On conducting the same analysis of text 2
 
 
