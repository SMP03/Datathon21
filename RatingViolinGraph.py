import json
import numpy as np
import matplotlib.pyplot as plt


def rate(e):
    return e["rating"]


dataset = json.load(open("train_reviews.json", "r")) #Dataset


rest_ratings = []
for i in range(0,len(dataset)-1):
    rating = dataset[i]["rating"]
    title = dataset[i]["title"]
    x_cor = dataset[i]["gps_coordinates"]["longitude"]
    y_cor = dataset[i]["gps_coordinates"]["latitude"]
    rest_ratings.append({"rating": rating,
                         "title": title,
                         "coords": [x_cor, y_cor]})
rest_ratings.sort(key=rate, reverse=True)

rating = []
for i in range(len(rest_ratings)):
    rating.append(rest_ratings[i]["rating"])

fig = plt.figure()

# Create an axes instance
ax = fig.add_axes([0,0, 1, 1])

# Create the boxplot
bp = ax.violinplot(rating, showmeans=True)
print(np.average(rating))
plt.show()

