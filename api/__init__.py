#!/usr/bin/env python3

import logging

from decouple import config
from dotenv import load_dotenv

from flask import Flask 

APP = Flask(__name__)
LOG = logging.getLogger("optimal-price")
logging.basicConfig(level=logging.DEBUG)

from api import routes
