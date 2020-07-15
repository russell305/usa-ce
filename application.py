# set FLASK_APP=application.py

# export DATABASE_URL="postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p"


# put link on sign-in page to other courses...need to take more courses?

# fix title tags

#p tags need to have font size or make h-tag,for SEO. after all templates done.



#fix wrong password and cancel, there are duplicates

#adminer /

#test stripe black background

#heroku logs --tail
# heroku add ons
# move pa-image into folder do this last

from flask import Flask, render_template, request, session, jsonify, redirect, url_for# Import the class `Flask` from the `flask` module, written by someone else.
from flask_session import Session
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from pandas import read_csv
import json #for Python to Javascript
import requests #for JSON
import stripe
import hashlib #password
import re  #regex
import datetime
import math
import csv


app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# from flask_sslify import SSLify
# sslify = SSLify(app)

# Session (app)
# engine = create_engine("postgres://iykazvclamrzem:140bdec1e446a9119d4fb1c9e20d89fb17716e702de72b7be09f2b2e53b86d36@ec2-50-19-127-115.compute-1.amazonaws.com:5432/d134n6bd1767sd")
#talk to datbase wiTh SQL. Object used to manage connections to database.
#Sending data to and from database.
# db = scoped_session(sessionmaker(bind=engine)) # for individual sessions

#


@app.route("/", methods = ["GET", "POST"])
def index():

	return "index"
