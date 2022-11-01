# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/sophia/')  # connects /stub/ URL to stub() function
def sophia():
    return render_template("sophia.html")


@app.route('/haeryn/')  # connects /stub/ URL to stub() function
def haeryn():
    return render_template("haeryn.html")


@app.route('/annika/')  # connects /stub/ URL to stub() function
def annika():
    return render_template("annika.html")

@app.route('/groupproject/')  # connects /stub/ URL to stub() function
def groupproject():
    return render_template("groupproject.html")

@app.route('/grouproles')
def grouproles():
    return render_template("grouproles.html")

@app.route('/sprint')
def sprint():
    return render_template("sprint.html")

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
