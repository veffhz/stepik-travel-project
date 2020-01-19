import random

from flask import Flask
from flask import render_template
from werkzeug import exceptions

from data.dataset import title, titles
from data.dataset import tours, departures

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title=title, titles=titles,
                           departures=departures, tours=tours)


@app.route('/from/<direction>')
def get_direction(direction):
    filtered_tours = {k: v for k, v in tours.items() if v['departure'] == direction}
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


@app.template_filter('limit')
def limit(dictionary, n):
    return random.sample(dictionary.items(), n)


@app.template_filter('split')
def split(items, key, n):
    return items.get(key).split()[n]


if __name__ == '__main__':
    app.run()
