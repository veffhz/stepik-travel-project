from flask import render_template
from werkzeug import exceptions

from application import app
from application.data.dataset import title, titles
from application.data.dataset import tours, departures
from application.data_helper import random_limit, filter_tours


@app.route('/')
def main():
    random_tours = random_limit(tours, 6)
    return render_template('index.html', title=title, titles=titles,
                           departures=departures, tours=random_tours)


@app.route('/from/<direction>')
def get_direction(direction):
    filtered_tours = filter_tours(direction, tours)
    return render_template('direction.html', title=title,
                           departures=departures,
                           tours=filtered_tours, direction=direction)


@app.route('/tours/<int:tour_id>')
def get_tour(tour_id):
    tour = tours[tour_id]
    return render_template('tour.html', title=title,
                           tour=tour, departures=departures)


@app.errorhandler(exceptions.NotFound)
def not_found(e):
    return render_template("404.html"), e.code


@app.errorhandler(exceptions.InternalServerError)
def server_error(e):
    return render_template("500.html"), e.code
