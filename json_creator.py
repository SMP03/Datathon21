import json

# Crop Restaurants to coordinates to keep only Barcelona's
# and return a json only with their coords and rating

BBox = (2.05, 2.234, 41.339, 41.4609) #Bounding Box

def rate(e):
    return e["rating"]

y = json.load(open("train_reviews.json", "r"))


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
    if (xcor > BBox[0] and xcor < BBox[1] and ycor > BBox[2] and ycor < BBox[3]):
        x.append(i["coords"][0])
        y.append(i["coords"][1])
        rating.append(i["rating"])

json_file = {"x": x, "y": y, "rating":rating}

with open('CoordsRating.json', 'w') as jsonfile:
    json.dump(json_file, jsonfile)
