import matplotlib.pyplot as plt
import numpy as np
import json
import math
from PIL import Image, ImageOps

def distance(x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2+(y1-y0)**2)

def mapea(val, min0, max0, min1, max1):
    val -= min0
    val /= (max0-min0)
    val *= (max1-min1)
    val += min1
    return val;

def gauss(x, a, c):
    return a*math.exp(-(x**2/(2*c**2)))

mapa = Image.open("map_4.png") #Already cropped map from openstreetmap.org
print(mapa.format)
print(mapa.size)
print(mapa.mode)


image = np.asarray(mapa)
pixels = (image.shape[0], image.shape[1])
map_area = ((2.05, 2.234),
            (41.339, 41.4609))

c = 20

with open('CoordsRating.json', 'r') as jsonfile:
    arxiu = json.load(jsonfile)

xs = arxiu["x"]
ys = arxiu["y"]
rating = arxiu["rating"]

avg = np.average(rating)

for i in range(len(xs)):
    xs[i] = round(mapea(xs[i], map_area[0][0], map_area[0][1], 0, pixels[0]))
    ys[i] = round(mapea(ys[i], map_area[1][0], map_area[1][1], 0, pixels[1]))


heat = np.empty((pixels[0], pixels[1], 4))
print(image.shape)
print(heat.shape)
print(heat[0][0].size)
for x in range(pixels[0]-1):
    for y in range(pixels[1]-1):
        hot = 0
        for r in range(len(rating)):
            d = distance(x, pixels[1]-y-1, xs[r], ys[r])
            hot += max(c-d, 0)*(rating[r]-avg)/5*c
        
        if hot > 0:
            heat[x][y] = np.asarray(image[x][y] + (0, hot, 0, 0))
            heat[x][y].clip(min=0, max=255)
        else:
            heat[x][y] = np.asarray(image[x][y] - (hot, 0, 0, 0))
            heat[x][y].clip(min=0, max=255)
        

img = Image.fromarray(np.uint8(heat), mode="RGBA")
img.save("HeatMap.png")


