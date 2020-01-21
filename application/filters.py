import random

from flask import current_app as app


@app.template_filter('limit')
def limit(dictionary, n):
    return random.sample(dictionary.items(), n)


@app.template_filter('split')
def split(items, key, n):
    return items.get(key).split()[n]


@app.template_filter('thousand')
def thousand(price):
    return f'{price:,d}'.replace(',', ' ')
