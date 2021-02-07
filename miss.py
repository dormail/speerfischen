# miss.py
# function calculating the distance by which the fisher misses the fish
import numpy as np

def miss(alpha, dist=1, depth=1.5, h=2):
    # vectors for fisher and fish and direction in which fisher throws
    r0 = np.array([0,h,0])
    fish = np.array([dist, -1* depth, 0])
    direc = np.array([np.sin(alpha), -1 * np.cos(alpha), 0])

    d = np.linalg.norm(np.cross(direc, r0 - fish))
    return d

