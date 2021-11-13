import matplotlib.pyplot as plt
import numpy as np
import json

def rate(e):
    return e["rating"]

y = json.load(open("/home/sergi/Datathon21/train_reviews.json", "r"))


rest_ratings = []
for i in range(0,len(y)-1):
    rating = y[i]["rating"]
    title = y[i]["title"]
    x_cor = y[i]["gps_coordinates"]["longitude"]
    y_cor = y[i]["gps_coordinates"]["latitude"]
    rest_ratings.append({"rating": rating,
                         "title": title,
                         "coords": [x_cor, y_cor]})
rest_ratings.sort(key=rate)

x = []
y = []
rating = []

for i in rest_ratings:
    xcor = i["coords"][0]
    ycor = i["coords"][1]
    if (xcor > 2 and xcor < 2.35 and ycor > 41.33 and ycor < 41.475):
        x.append(i["coords"][0])
        y.append(i["coords"][1])
        rating.append(i["rating"])

mapita = plt.imread('map.png')

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(x, y, c=rating, cmap="gist_rainbow",zorder=1, s=10)
ax.set_title('Plotting Spatial Data on Riyadh Map')
BBox = [2, 2.35, 41.33, 41.475]

ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(mapita, zorder=0, extent = BBox, aspect= 'equal')

plt.show()
