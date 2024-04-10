from textblob import TextBlob
from textblob import Word
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from googletrans import Translator


text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)
print("Senetences: ")
print(blob.sentences)   
# Output: [Sentence("Today is a beautiful day."), Sentence("Tomorrow looks like bad weather.")]

print("Words: ")
print(blob.words)       
# Output: ['Today', 'is', 'a', 'beautiful', 'day', 'Tomorrow', 'looks', 'like', 'bad', 'weather']

print("Tags: ")
print(blob.tags)        
# Output: [('Today', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('beautiful', 'JJ'), ('day', 'NN'), ('Tomorrow', 'NNP'), ('looks', 'VBZ'), ('like', 'IN'), ('bad', 'JJ'), ('weather', 'NN')]
# NN stands for noun, VBZ stands for verb, DT stands for determiner, JJ stands for adjective, IN stands for preposition

print("Noun Phrases: ")
#print(blob.noun_phrases)
# Output: ['beautiful day', 'bad weather']

print("Sentiment: ")
print(blob.sentiment)
# Sentiment -1.0 to 1.0, where -1.0 is negative and 1.0 is positive
# Subjectivity 0.0 to 1.0, where 0.0 is objective and 1.0 is subjective
# Output: Sentiment(polarity=0.0, subjectivity=0.0)
'''
#Detecting language
# detect_language() and translate() are deprecated in TextBlob 0.15.3. Using instead googletrans
translator = Translator()
print("Language: ")
translator.detect('Hola')
#print(translator.detect('This sentence is written in English.'))
# Output: en
'''

index = Word('index')

# Pluralize the word index
print(index.pluralize())

cacti = Word('cacti')
# Singularize the word cacti
print(cacti.singularize())

animals = TextBlob('dog cat fish bird').words

# Pluralize the words in the list
print(animals.pluralize())

# Spellcheck
word = Word('theyr')
print(word.spellcheck())
# Output: [('they', 0.5714285714285714), ('their', 0.42857142857142855)]
print("Corrected word: ", word.correct())

# Correcting sentences
sentence = TextBlob('Ths sentense has missplled wrds.')
print("Corrected sentence: ", sentence.correct())

# Lemmatization
# Stemming removes a prefix or suffix from a word leaving only a stem. It may or may not be real world.
# Capitalization is not considered in stemming.
# Lemmatization is a more advanced technique that considers the context and converts the word to its base form.
word = Word('varieties')
print("Stemmed word: ", word.stem())
print("Lemmatized word: ", word.lemmatize()) 

# Word Frequencies
blob = TextBlob(Path("C:\\Users\\gabe_\\OneDrive\\Documents\\GitHub\\CIS2532\\Week 7\\RomeoJuliet.txt").read_text()) 

# Access the word frequencies through the TextBlob's word_counts dictionary
print(blob.word_counts['juliet'])
# Output: 178
print(blob.word_counts['romeo'])
# Output: 299
print(blob.word_counts['thou'])
# output: 277

# Definitions
happy = Word('happy')
print(happy.definitions)

# Synonyms
print("Definition of happy:")
print(happy.synsets)
# Output: [Synset('happy.a.01'), Synset('felicitous.s.02'), Synset('glad.s.02'), Synset('happy.s.04')]

# Each synset has a list of lemmas
synonym = set()
for synset in happy.synsets:
    for lemma in synset.lemmas():
        synonym.add(lemma.name())
# Output: {'felicitous', 'glad', 'happy', 'well-chosen'}

# Antonyms
# If the word represented by a Lemmahas anthpnyms, invoking the Lemma's antonyms method
# returns a list of antonyms.
print("Antonyms of happy:" )
lemmas = happy.synsets[0].lemmas()
#print(lemmas())
print(lemmas[0].antonyms())
# Output: [Lemma('unhappy.a.01.unhappy')]


# NLTK -> Natural Language Toolkit
nltk.download('stopwords')
stops = stopwords.words('english')
blob = TextBlob("Today is a beautiful day.")
print([word for word in blob.words if word not in stops])

# N-grams
# n-gram method produces a list of n-grams from the text.

text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)

print("N-grams: ")
print(blob.ngrams(n=5))

