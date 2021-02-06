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
h = (dist - np.tan(alpha) * depth) / np.tan(np.arcsin(n_wt * np.sin(alpha)))
print(f'h = {h}')

plt.plot(a, y2,
        label=r'$h(\alpha)$')
plt.plot(np.linspace(0.2, 0.3), np.linspace(2,2),
        label=r'Augenhöhe des Fischers bei 2m',
        color='r',
        ls='--')
plt.plot(a, np.abs(y2 - 2),
        label=r'$\vert h(\alpha) - 2\si{m}\vert$')

plt.title(rf'Plot für Höhe des Strahls bei $y=0$ (ohne Luftschicht)')

plt.legend()
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$1/$m')
plt.savefig('plot-2a.pdf')
