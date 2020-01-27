import random

from flask import current_app as app


@app.template_filter('limit')
def limit(dictionary, quantity):
    if len(dictionary) < quantity:
        return random.sample(dictionary.items(), len(dictionary))
    return random.sample(dictionary.items(), quantity)


@app.template_filter('split')
def split(items, key, num):
    item = items.get(key)
    if item:
        return items.get(key).split()[num]
    else:
        return key


@app.template_filter('thousand')
def thousand(price):
    if price and isinstance(price, int):
        return f'{price:,d}'.replace(',', ' ')
    elif isinstance(price, float):
        return f'{price:.3f}'.replace('.', ' ')
    else:
        return f'{price}'
