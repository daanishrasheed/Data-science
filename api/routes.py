#!/usr/bin/env python3

import logging
from flask import request, jsonify, render_template

from api import APP
from api.service import location_service
from api.service import price_service

LOG = logging.getLogger("optimal-price")

@APP.route("/lookup-neighborhood", methods=["GET", "POST"])
def lookup_neighborhood():
    """
        Endpoint for looking up a neighborhood from a pair of coordinates.

        Expects "latitude" and "longitude" URL parameters as floats.

        Returns a json object containing the neighborhood.
    """

    if request.method == "GET":
        lat = float(request.args.get("latitude"))
        long = float(request.args.get("longitude"))

    elif request.method == "POST":
        lat = float(request.form["latitude"])
        long = float(request.form["longitude"])

    result = location_service.get_neighborhood(lat, long)
    
    return jsonify({
        "neighborhood": result
    })

@APP.route("/lookup-neighborhood-form")
def lookup_neighborhood_form():
    return render_template("coords-form.html")


@APP.route("/estimate-price", methods=["POST"])
def estimate_price():
   neighborhood = request.form["neighborhood"] 
   room_type = request.form["neighborhood"] 
   listings_count = int(request.form["listings_count"])
   num_reviews = int(request.form["num_reviews"])
   min_nights = int(request.form["min_nights"])
   availability_365 = int(request.form["availability"])
   last_review_time = int(request.form["last_review_time"])

   price = price_service.estimate(
       neighborhood=neighborhood,
       room_type=room_type,
       min_nights=min_nights,
       num_reviews=num_reviews,
       listings_count=listings_count,
       availability_365=availability_365,
       last_review=last_review_time,
    )

   return jsonify({
       "price": price
    })

@APP.route("/estimate-price-form")
def estimate_price_form():
    return render_template("price-form.html")
