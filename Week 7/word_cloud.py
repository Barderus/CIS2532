from pathlib import Path
import imageio.v2 as imageio
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = Path(r"RomeoAndJuliet.txt").read_text()

# WordCloud fills non-white areas of a mask image with text
# Load the mask using the imread function from the imageio module
mask_image = imageio.imread(r"mask_heart.png")

# Configure the WorldCloud object
'''
    400x200 pixels, unless specified otherwise with the width and height parameters
    If you don't specify the mask image's width and height, the WordCloud object will use the mask image's dimensions
    WordCloud assigns random colors from a color map
'''
wordCloud = WordCloud(width = 1000, height=1000, colormap='prism', mask=mask_image, background_color='white')

# Generating the word cloud
# The generate method creates a word cloud from the text
wordCloud = wordCloud.generate(text)

# Saving the word cloud as an image
wordCloud.to_file("RomeoJulietHeart1.png")

plt.imshow(wordCloud)
