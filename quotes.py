from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
quotes_api = Blueprint('quotes_api', __name__,
                   url_prefix='/api/quotes')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(quotes_api)



def getAPI():


    url = "https://inspiring-quotes.p.rapidapi.com/random"

    headers = {
        "X-RapidAPI-Key": "222daebd02msh197e0db183672fap17cc9djsn8a1f2f813e5b",
        "X-RapidAPI-Host": "inspiring-quotes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    quote_data = response
    return response


if __name__ == "__main__": 

    # This code looks for "world data"
    response = getAPI()
    quote = response.json().get('quote')
    person = response.json().get('author')