import os
import sys

from flask import Flask, session, render_template, request, flash, redirect, abort
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)

# fix windows terminal issue on my computer
if sys.platform.lower() == "win64":
    os.system('color')

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

# need to remove existing geojson layer every time there is a new query - filter wont apply to existing data

@app.route("/dates", methods=['POST'])
def dates():
    # get from and to dates from the date picker
    fr = request.form.get("from")
    to = request.form.get("to")
    url = "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate > '"+fr+"' and issueddate < '"+to+"'&$select=issueddate,workclassgroup,contractorname,communityname,originaladdress"

    data = requests.get(url)
    # convert
    return render_template("index.html")
