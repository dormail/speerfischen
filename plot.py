# plot.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'results-a.csv'
df = pd.read_csv(filename)

a = df['a']
y2 = df['y2']

res = np.abs(y2 - 2).argmin()
best_angle = a[res]

print(f'The best angle was found to be {best_angle}.')



plt.plot(a, np.abs(y2 - 2))
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$(y_2 - h) / $m')
plt.show()
