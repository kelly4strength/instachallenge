"""Instachallenge - Write an app that takes a hashtag, start date, and end date, 
and collects submissions from Instagram """
# Backend: Provide an API that accepts a POST to create a collection and GET to retrieve content 

# from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db
# User, List, Location, Category, Item, copy_items_to_db

# from instagram import client, subscriptions

app = Flask(__name__)

# For debug toolbar
app.secret_key = "ABC"

# Defining variable for Jinja2 to avoid it failing silently (this raises and error)
# app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """landing page"""
    return render_template ("form.html")

    # construct a string - concatenate the info that comes in
    # what's the python magic to call the URL and get the data back

@app.route('/results', methods=["POST"])
def show_results():

    hashtag = request.form.get("hashtag")
    # startDate = request.form.get("startDate")
    # endDate = request.form.get("endDate")

    endpoint = "https://api.instagram.com/v1/tags/" + hashtag + "/media/recent?access_token=272855367.b6f7db4.27aee70b486a4fd7b1b5546c1da0453d"

    return redirect (endpoint)
    # return render_template ("results.html", hashtag=hashtag, endpoint=endpoint)
# Endpoint: https://api.instagram.com/v1/tags/poorhoffermobile/media/recent?access_token=272855367.b6f7db4.27aee70b486a4fd7b1b5546c1da0453d

 
if __name__ == "__main__":

    app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()





