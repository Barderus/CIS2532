from textblob import TextBlob
from textblob import Word
from pathlib import Path
from operator import itemgetter
import pandas as pd
import requests
from bs4 import BeautifulSoup
import imageio.v2 as imageio
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

''' 
    12-1 Using the request library to download the pytho.org home page content and then use the Beautiful Soup Library to extract only the text
from the page. Eliminate stop words in the resulting text, then use the wordcloud module to create a word cloud based on the text.
'''
nltk.download("stopwords")
nltk.download('stopwords')
stops = stopwords.words('english')


response = requests.get("https://www.python.org")
response.content # Give back the page's HTML
soup = BeautifulSoup(response.content, "html5lib")
text = soup.get_text(strip=True)

# Remove stop words
filtered_text = ' '.join([word for word in text.split() if word.lower() not in stops])


# Load the mask using the imread function from the imageio module
mask_image = imageio.imread(r"Week 7\mask_circle.png")

wordCloud = WordCloud(width = 1000, height=1000, colormap='prism', mask=mask_image, background_color='white')
wordCloud = wordCloud.generate(filtered_text)

# Saving the word cloud as an image
wordCloud.to_file("WB.png")

plt.imshow(wordCloud)

'''
    12.2 Create a Textblob based on the text from Python Org and then tokenize it into sentences and words, 
    and extract its noun prahses.
'''

blob = TextBlob(filtered_text)

print("\nSenetences: ")
print(blob.sentences) 

print("\nWords: ")
print(blob.words)

print("\nNoun phrases:")
print(blob.noun_phrases) 

'''
    12.3 Download a web page for a current news article and create a Textblob. Display the sentiment for the 
entire Textblob and for each sentence
'''

response = requests.get("https://chicago.suntimes.com/columnists/2024/04/09/museum-science-industry-msi-chicago-closed-military-artifacts-pentagon-secretary-state-bomb-squad")
response.content # Give back the page's HTML
soup = BeautifulSoup(response.content, "html5lib")
text = soup.get_text(strip=True)

blob = TextBlob(text)
#print(blob.sentiment)

for sentence in blob.sentences:
    sentiment = sentence.sentiment
    print(sentence)
    print(f"Sentiment: Polarity={sentiment.polarity}, Subjectivity={sentiment.subjectivity}")
    print()

'''
    12.6 Create a top-20 word frequency bar chart and a word cloud, based on Shakespeare's Hamlet. Use the mask.oval.png file.
'''

''' Top 20 word frequency bar chart '''
text = Path(r"Week 7\Hamlet.txt").read_text()
blob = TextBlob(text)
stop_words = stopwords.words('english')

# Getting the words frequencies
items = blob.word_counts.items()

# Eliminating the stop words
items = [item for item in items if item[0] not in stop_words]

# Sorting the words by frequency
sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Getting the top 20 words
top20 = sorted_items[0:20]

# Convert the top 20 words to a DataFrame
df = pd.DataFrame(top20, columns=['word', 'count'])
print(df)

# Reset index for proper alignment
df = df.reset_index(drop=True)

# Plotting as vertical bars
axes = df.plot(kind='barh', x='word', y='count', legend=False)
plt.gcf().tight_layout()
plt.show()

''' Wordcloud based on the top 20 word frequency '''

# Load the mask using the imread function from the imageio module
mask_image = imageio.imread(r"Week 7\mask_oval.png")

# Configure the WorldCloud object
wordCloud = WordCloud(width = 1000, height=1000, colormap='prism', mask=mask_image, background_color='white')

# Generating the word cloud
wordCloud = wordCloud.generate(text)

# Saving the word cloud as an image
wordCloud.to_file("HamletCloud.png")

plt.imshow(wordCloud)