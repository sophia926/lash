from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
covid_api = Blueprint('gratitude_api', __name__,
                   url_prefix='/api/gratitude')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(covid_api)



def getAPI():
    global covid_data  # the covid_data global is preserved between calls to function
    try: covid_data
    except: covid_data = None


    url = "https://gratitude-questions.p.rapidapi.com/question"

    headers = {
        "X-RapidAPI-Key": "222daebd02msh197e0db183672fap17cc9djsn8a1f2f813e5b",
        "X-RapidAPI-Host": "gratitude-questions.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    gratitude_data = response
    return response


if __name__ == "__main__": 

    # This code looks for "world data"
    response = getAPI()
    print("World Totals")
    world = response.json().get('question')