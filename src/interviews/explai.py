"""
Explai interview

At an eCommerce company, parcels needs to be packed. 
It should contain the following 4 items stored in warehouses at different geo locations:

items = [
    {"id": 123, "wh": "erfurt", "geolocation": (50.9787, 11.03283)},
    {"id": 456, "wh": "stradella", "geolocation": (45.07445, 9.30169)},
    {"id": 789, "wh": "lahr", "geolocation": (48.34042, 7.86886)},
    {"id": 102, "wh": "gryfino", "geolocation": (53.25243, 14.48831)}
    ]

Write a function that finds the warehouse where all the items should be collected, 
so that they have to be transported the smallest distance possible.
"""
import math

def euclidean_distance(location1: tuple, location2: tuple):
    dist = math.sqrt((location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)
    return dist


def find_min_distance(items: list[dict]):

    n =len(items)
    min_dist = []

    for i in range(n):
        dist = 0
        for j in range(n):
            if i != j:
                dist += euclidean_distance(items[i]["geolocation"], items[j]["geolocation"]) 
        
        min_dist.append(dist)

    location = items[min_dist.index(min(min_dist))]
    return location
        

if __name__ == "__main__":
    # location1 = (50.9787, 11.03283)
    # location2 = (45.07445, 9.30169)

    # dist = euclidean_distance(location1=location1, location2=location2)
    # print(dist)

    items = [
    {"id": 456, "wh": "stradella", "geolocation": (45.07445, 9.30169)},
    {"id": 123, "wh": "erfurt", "geolocation": (50.9787, 11.03283)},
    {"id": 789, "wh": "lahr", "geolocation": (48.34042, 7.86886)},
    {"id": 102, "wh": "gryfino", "geolocation": (53.25243, 14.48831)}
    ]

    res = find_min_distance(items=items)
    print(res)

