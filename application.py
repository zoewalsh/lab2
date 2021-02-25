import os
import sys

from flask import Flask, session, render_template, request, flash, redirect, abort, jsonify
from flask_session import Session
import requests
import geojson
import json

app = Flask(__name__)

# fix windows terminal issue on my computer
if sys.platform.lower() == "win64":
    os.system('color')

# default route, no data is passed to index
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

# when dates are passed, feed data to index
@app.route("/dates", methods=['POST'])
def dates():
    app_token="Htp39ZMQbN1AmuufzF1ZlgdFt"
    # get from and to dates from the date picker
    fr = request.form.get("from")
    to = request.form.get("to")
    url = "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate > '"+fr+"' and issueddate < '"+to+"'"
    # request with url
    data = requests.get(url).json()
    # get only features
    data2 = data['features']
    return render_template("index.html",data=data2)
