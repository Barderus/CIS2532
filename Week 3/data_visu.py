import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

rolls = [random.randrange(1, 7) for i in range(1000000000)]

values, frequencies = np.unique(rolls, return_counts=True)

# Bar Plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')  # Set seaborn style

# Create and display the bar plot
plt.figure(figsize=(8, 6))
axes = sns.barplot(x=values, y=frequencies)

# Set the title of the plot
axes.set_title(title)

# Label the axes
axes.set(xlabel='Die Value', ylabel='Frequency')

# Scale the y-axis to add room for text above bars
axes.set_ylim(top=max(frequencies) * 1.10)

# Create and display the text for each bar
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text,
              fontsize=11, ha='center', va='bottom')

plt.show()
