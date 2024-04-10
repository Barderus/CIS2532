from pathlib import Path
from textblob import TextBlob
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt

blob = TextBlob(Path("C:\\Users\\gabe_\\OneDrive\\Documents\\GitHub\\CIS2532\\Week 7\\RomeoJuliet.txt").read_text())
stop_words = stopwords.words('english')

# Getting the words frequencies
items = blob.word_counts.items()

# Eliminating the stop words
items = [item for item in items if item[0] not in stop_words]

# Sorting the words by frequency
sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Getting the top 20 words
''' 
TextBlob tokenization splits all contractions at their apostrophes and counts
the total number of apostrophes as one of the words.
    If you display sorted_item[0], you will see that the first word is 'thou'.
    We ignore element 0
'''
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