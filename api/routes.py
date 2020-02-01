#!/usr/bin/env python3

import logging
from flask import request, jsonify, render_template

from api import APP
from api.service import location_service

LOG = logging.getLogger("optimal-price")

@APP.route("/lookup-neighborhood", methods=["GET", "POST"])
def lookup_neighborhood():

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
