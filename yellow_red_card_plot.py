import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pandas.DataFrame(np.c_[dataset['general_card_yellow'],dataset['general_card_red']], index=dataset['Team'])
my_colors = 'yr'
df.plot(kind='bar', color=my_colors)



red_patch = mpatches.Patch(color='yellow', label='Yellow Cards')
orange_patch = mpatches.Patch(color='red', label = 'Red Cards')
plt.legend(handles=[orange_patch, red_patch])

plt.xticks(rotation=90)

plt.show()