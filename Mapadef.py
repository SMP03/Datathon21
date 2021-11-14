import matplotlib.pyplot as plt
import numpy as np
import json

# Add points to the heatmap

with open('CoordsRating.json', 'r') as jsonfile:
    arxiu = json.load(jsonfile)

x = arxiu["x"]
y = arxiu["y"]
rating = arxiu["rating"]

heatmap = plt.imread('HeatMap.png')
image = np.asarray(heatmap)

fig, ax = plt.subplots(figsize = (8,7))
im = ax.scatter(x, y, c=rating, cmap="gist_rainbow",zorder=1, s=10)

BBox = (2.05, 2.234, 41.339, 41.4609)

ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(heatmap, zorder=0, extent = BBox, aspect= 'equal')

fig.colorbar(im, ax=ax)
plt.show()
