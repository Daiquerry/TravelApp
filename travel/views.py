from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

# identifies the route for the index landing page and the forms to be displayed
@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()
    return render_template('index.html', destination=destinations)

# identifies the search route and the forms to be displayed
# has an if statement that will also account for user search inputs that will return events that contain what they enter into the text field
# if nothing has been found it returns to index making it look like nothing has happened 
@mainbp.route('/search')
def search():
    if (request.args['search'] and request.args['search'] != ""):
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        print(destinations)
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))