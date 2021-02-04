# 2a.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('pgf')

PI = np.pi

filename = 'results-a.csv'
df = pd.read_csv(filename)

a = df['a']
y2 = df['y2']

res = np.abs(y2 - 2).argmin()
best_angle = a[res]
angle_arrive = df['b'][res]

print(f'The best angle was found to be {best_angle}.')
print(f'The light arrives at the fishers eye at angle {angle_arrive}.')

# kontrollrechnung
alpha = best_angle
dist = 1
depth = 1.5
n_wt = 1.33
h = (dist - np.sin(alpha) * depth) / np.tan(np.arcsin(n_wt * np.sin(alpha)))
print(f'h = {h}')

plt.plot(a, np.abs(y2 - 2))
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\vert y_2 - h \vert / $m')
plt.savefig('plot-2a.pdf')
