import random

from flask import current_app as app


@app.template_filter('limit')
def limit(dictionary, n):
    if len(dictionary) < n:
        return random.sample(dictionary.items(), len(dictionary))
    return random.sample(dictionary.items(), n)


@app.template_filter('split')
def split(items, key, n):
    item = items.get(key)
    if item:
        return items.get(key).split()[n]
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
