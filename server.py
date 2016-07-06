"""Instachallenge - Write an app that takes a hashtag, start date, and end date, 
and collects submissions from Instagram """
# Backend: Provide an API that accepts a POST to create a collection and GET to retrieve content 

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Search
 
# from helper import get_endpoint_data

import requests

import json

import datetime
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
    # Take in start and end dates from users and turn them into datetime > happens in the db!
    
    # adding search parameters to instas db
    new_search = Search(tag=tag,
                    start_date=start_date, 
                    end_date=end_date)
    db.session.add(new_search)
    db.session.commit()

    # urls = get_endpoint_data(tag)

        # concatenate the endpoint url and given hashtag to construct the url
    endpoint = "https://api.instagram.com/v1/tags/" + tag + "/media/recent?access_token=272855367.b6f7db4.27aee70b486a4fd7b1b5546c1da0453d"
        
        # use the python requests library to call the endpoint URL and get the data (type(r)='requests.models.Response')
    r = requests.get(endpoint)
        
        # Confirming response is good (200)
    print r.status_code
        
        # set the response to json (dict)
    huge_data = r.json()

    # For loop that loops over the huge_data[data] dictionary 
    # and gets urls for each image in the response list and puts them in urls[]
    
    urls = []

    for i in huge_data['data']:
        image_url = i['images']['thumbnail']['url']
        print image_url
        caption_time = i['caption']['created_time']
        # print caption_time
        caption_datetime = (datetime.datetime.fromtimestamp(int(caption_time)).strftime('%Y-%m-%d %H:%M:%S'))
        caption_datetime_too = (datetime.datetime.strptime(caption_datetime,'%Y-%m-%d %H:%M:%S'))
        # print "caption_datetime"
        # print caption_datetime
        # print type(caption_datetime)

        # print caption_datetime_too
        # print type(caption_datetime_too)

        start_date = new_search.start_date
        print "start_date"
        print type(start_date)
        end_date = new_search.end_date
        print end_date

        if new_search.start_date <= caption_datetime_too >= new_search.end_date:
        # 2016-07-03 <= 2016-06-30 20:53:03 >=2016-07-05

            urls.append(image_url)
            print urls
        # return urls


    # if caption_time is between start_date and end_date
    # then include these images in the response data

    # "data": 
        # user": {"username": "kelly4strength", 
            # "profile_picture": "https://scontent.cdninstagram.com/t51.2885-19/10865062_1630836193858815_1047750309_a.jpg", 
            # "id": "1094228", "full_name": "Kelly Hoffer"



    return render_template ("results.html", tag=tag, urls=urls)
 
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()





