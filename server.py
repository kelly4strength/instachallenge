"""Instachallenge - Write an app that takes a hashtag, start date, and end date, 
and collects submissions from Instagram """
# Backend: Provide an API that accepts a POST to create a collection and GET to retrieve content 

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Search

import requests

import json

from datetime import datetime
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

    tag = request.form.get("tag")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")

    # adding search prameters to instas db
    new_search = Search(tag=tag,
                    start_date=start_date, 
                    end_date=end_date)
    db.session.add(new_search)
    db.session.commit()

    # concatenate the endpoint url and given hashtag to construct the url
    endpoint = "https://api.instagram.com/v1/tags/" + tag + "/media/recent?access_token=272855367.b6f7db4.27aee70b486a4fd7b1b5546c1da0453d"
    
    # use the python requests library to call the endpoint URL and get the data (type(r)='requests.models.Response')
    r = requests.get(endpoint)
    
    # set the response to json (dict)
    huge_data = r.json()

    # test_url work but only gets you the url at index [0]
    test_url = huge_data['data'][0]['images']['standard_resolution']['url']

    # I need to set up a for loop that loops over the huge_data dictionary 
    # and gets the data for each individual image in the response list
    
    # urls = []
    # for i in test_url:
    

    #     test_url = huge_data['data'][0]['images']['standard_resolution']['url']
    #     urls.append(test_url)
    # return urls


# def get_item_choices(category_names):
#     """pass categories into copied items"""
#     categories = []

#     for category_name in category_names:
#         if category_name:
#             category = Category.query.filter_by(category_name=category_name).one()
#             category_id = category.category_id   
#             categories.append(category_id)
#     return categories

    return render_template ("results.html", tag=tag, test_url=test_url)
 
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()





