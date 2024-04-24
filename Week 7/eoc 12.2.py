import spacy
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from textatistic import Textatistic

# 12.7
'''
    Download several news siyes current news articles on the sam etopic. 
    Perform readability assessments on them to determine which sites are the most readable.
    For each article, calculae the avrage nymber of words per sentence, the average number of characters per word and 
    the average nmbers of syllables per word.
'''
#nltk.download("stopwords")
#nltk.download('stopwords')
stops = stopwords.words('english')


article1 = requests.get("https://abc7chicago.com/ohare-airport-chicago-traffic-protest-kennedy-expressway-i90/14668476/")
article1.content # Give back the page's HTML
soupArt1 = BeautifulSoup(article1.content, "html.parser")
text = soupArt1.get_text(strip=True)
filtered_text1 = ' '.join([word for word in text.split() if word.lower() not in stops])

readability1 = Textatistic(filtered_text1)


article2 = requests.get("https://www.nbcchicago.com/news/local/ohare-warns-of-substantial-traffic-delays-due-to-protest-blocking-kennedy-expressway-lanes/3410631/")
article2.content # Give back the page's HTML
soupArt2 = BeautifulSoup(article2.content, "html.parser")
text = soupArt2.get_text(strip=True)
filtered_text2 = ' '.join([word for word in text.split() if word.lower() not in stops])

readability2 = Textatistic(filtered_text2)



article3 = requests.get("https://www.chicagotribune.com/2024/04/15/protestors-block-highway-entering-ohare-airport/")
article3.content # Give back the page's HTML
soupArt3 = BeautifulSoup(article3.content, "html.parser")
text = soupArt3.get_text(strip=True)
filtered_text3 = ' '.join([word for word in text.split() if word.lower() not in stops])

readability3 = Textatistic(filtered_text3)


# Article 1
print("\nFor article1:")
print(f"Article 1 readability:\n {readability1.dict()}")

# Average number of words in a sentence
words = readability1.word_count
sentence = readability1.sent_count
avg = sentence / words
print(f"The average number of words in a sentence is: {avg}")

# Average number of char in a word
char = readability1.char_count
avg = words / char
print(f"The average number of characters in a word is: {avg}")

# Average number of syllables in a word
syllables = readability1.sybl_count
avg = words / syllables
print(f"The average number of syllables in a word is: {avg}")


# Article 2
print("\nFor article 2:")
print(f"Article 2 readability:\n {readability2.dict()}")

# Average number of words in a sentence
words = readability2.word_count
sentence = readability2.sent_count
avg = sentence / words
print(f"The average number of words in a sentence is: {avg}")

# Average number of char in a word
char = readability2.char_count
avg = words / char
print(f"The average number of characters in a word is: {avg}")

# Average number of syllables in a word
syllables = readability2.sybl_count
avg = words / syllables
print(f"The average number of syllables in a word is: {avg}")

# Article 3
print("For article 3: \n")
print(f"Article 3 readability:\n {readability3.dict()}")

# Average number of words in a sentence
words = readability3.word_count
sentence = readability3.sent_count
avg = sentence / words
print(f"The average number of words in a sentence is: {avg}")

# Average number of char in a word
char = readability3.char_count
avg = words / char
print(f"The average number of characters in a word is: {avg}")

# Average number of syllables in a word
syllables = readability3.sybl_count
avg = words / syllables
print(f"The average number of syllables in a word is: {avg}")

# 12.8
'''
    Download a current news article then use the spaCy library's named entity recognition capabilities to display the 
    named entities (people, places, organization) in the article.
'''
nlp = spacy.load("en_core_web_sm")
spacyArt = requests.get("https://www.cnn.com/2024/04/16/tech/microsoft-g42-ai/index.html")
spacyArt.content # Give back the page's HTML
spacyArt = BeautifulSoup(spacyArt.content, "html.parser")
text = spacyArt.get_text(strip=True)
filtered_text = ' '.join([word for word in text.split() if word.lower() not in stops])

# Creating a spaCy Doc object
document = nlp(filtered_text)

print("\nNamed entities: ")
# Getting the named entities
for entity in document.ents:
    print(f"{entity.text}: {entity.label_}")

# 12.9
'''
    Download several news articles on the same topic and compare them for similarity.
'''
doc1 = nlp(filtered_text1)
doc2 = nlp(filtered_text3)
doc3 = nlp(filtered_text2)
print("\nSimilarity between article 1 and 2: ")
print(doc1.similarity(doc2))
print("\nSimilarity between article 1 and 3: ")
print(doc1.similarity(doc3))
print("\nSimilarity between article 2 and 3: ")
print(doc2.similarity(doc3))


