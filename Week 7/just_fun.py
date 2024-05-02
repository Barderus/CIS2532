'''
    Test
'''

from textblob import TextBlob
from textblob import Word
import nltk
from nltk.corpus import stopwords
import spacy
from textatistic import Textatistic


stops = stopwords.words('english')


text = r"C:\Users\gabe_\OneDrive\Desktop\College of Dupage\ENGLI 1102 - English Composition 2\Response.docx"
blob = TextBlob(text)

readability1 = Textatistic(blob)
