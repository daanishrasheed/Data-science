#!/usr/bin/env python3

import logging
from flask import request, jsonify

from api import APP
from api.service import location_service

LOG = logging.getLogger("optimal-price")

@APP.route("/lookup-neighborhood")
def lookup_neighborhood():

    lat = float(request.args.get("latitude"))
    long = float(request.args.get("longitude"))

    result = location_service.get_neighborhood(lat, long)
    
    return jsonify({
        "neighborhood": result
    })
