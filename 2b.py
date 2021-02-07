# 2b.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from miss import miss

mpl.use('pgf')
PI = np.pi

# Calculation for part b)
print('Aufgabe 2b)')

n1 = 1.33 # water
n2 = 1 # air
n = 1.1 # spicy air

hp = 1 # height of the spicy air
dh = 0.1 # thickness of the spicy air

a1 = np.linspace(0.1, 0.5)
a2 = np.arcsin(n1/n2 * np.sin(a1))
a3 = np.arcsin(n1/n * np.sin(a1))

d = 1
t = 1.5

h = (d - t * np.tan(a1) - hp * np.tan(a2) - dh * np.tan(a3)) / np.tan(a3) + hp + dh

# looking for a1 that matches h \approx 2
res = np.abs(h - 2).argmin()
best_angle = a1[res]
angle_arrive = a2[res]
print(f'The best angle was found to be {best_angle}.')
print(f'The light arrives at the fishers eye at angle {angle_arrive}.')

# calculating miss
d = miss(angle_arrive)
print(f'The fisher misses the fish by {d:.4f} m.')

plt.plot(a1, h,
        label=r'$h(\alpha_1)$')
plt.plot(a1, np.abs(h-2),
        label=r'$\vert h(\alpha_1) - 2m \vert$')
plt.plot(a1, np.linspace(2,2),
        color='r',
        label='Eyeheight = 2m')
plt.title(rf'Plot für Höhe des Strahls bei $y=0$ (mit Luftschicht)')
plt.legend()
plt.xlabel(r'$\alpha_1$')
plt.ylabel(r'1/m')

plt.savefig('plot-2b.pdf')
