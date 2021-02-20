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
