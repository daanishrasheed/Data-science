#!/usr/bin/env python3

"""
Contains utility functions pertaining to location.
"""

import json
from shapely.geometry import shape, GeometryCollection, Point


with open("data/neighbourhoods.geojson", "r") as f:
    js = json.load(f)

for feature in js["features"]:
    feature["poly"] = shape(feature["geometry"])

def get_neighborhood(lat, long):
    """
        Determins the neighborhood that a set of coordinates is in.

        @type lat: float
        @type long: float
        @rtype: str
    """
    p = Point(long, lat)
    for neighborhood in js["features"]:
        if neighborhood["poly"].contains(p):
            return neighborhood["properties"]["neighbourhood"]

    return ""
