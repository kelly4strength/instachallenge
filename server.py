"""Instachallenge - Write an app that takes a hashtag, start date, and end date, 
and collects submissions from Instagram """
# Backend: Provide an API that accepts a POST to create a collection and GET to retrieve content 

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Search

import requests

# from instagram import client, subscriptions

app = Flask(__name__)

# For debug toolbar
app.secret_key = "ABC"

# Defining variable for Jinja2 to avoid it failing silently (this raises and error)
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """landing page where user can input tag for search"""
    return render_template ("form.html")


@app.route('/results', methods=["POST"])
def show_results():
    """shows the results from the instagram endpoint url made with the inputted tag"""

    # r = requests.get('https://api.github.com', auth=('user', 'pass'))

    tag = request.form.get("tag")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")

    new_search = Search(tag=tag,
                    start_date=start_date, 
                    end_date=end_date)
    db.session.add(new_search)
    db.session.commit()

    # construct a string - concatenate the info that comes in
    endpoint = "https://api.instagram.com/v1/tags/" + tag + "/media/recent?access_token=272855367.b6f7db4.27aee70b486a4fd7b1b5546c1da0453d"
        # what's the python magic to call the URL and get the data back
    r = requests.get(endpoint)
    data = r.json()

    #how do I say get this data at the endpoint? 
    # and then take data from the end point which is a string and make it into a dict
    #then render the images found in the dict on the page?


    # "data": [{"attribution": null, 
    #         "tags": ["poorhoffermobile"], 
    #         "type": "image", 
    #         "location": null, 
    #         "comments": {"count": 0}, 
    #         "filter": "Normal", 
    #         "created_time": "1467345183", 
    #         "link": "https://www.instagram.com/p/BHTfEZtj9MF/", 
    #         "likes": {"count": 0}, 

    #         "images": {"low_resolution": {"url": "https://scontent.cdninstagram.com/
    #         t51.2885-15/s320x320/e35/11420918_132887830470925_116640902_n.jpg?
    #         ig_cache_key=MTI4NDUwNjk2MDY1ODQyMDQ4NQ%3D%3D.2", "width": 320, "height": 320}, 


    # return redirect (endpoint)
    return render_template ("results.html", data=data)
 
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()





