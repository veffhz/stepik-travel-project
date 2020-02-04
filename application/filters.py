from application import app


@app.template_filter('split')
def split(items, item_key, num):
    item = items.get(item_key)
    if item:
        return items.get(item_key).split()[num]
    else:
        return item_key


@app.template_filter('thousand')
def thousand(price):
    if price and isinstance(price, int):
        return f'{price:,d}'.replace(',', ' ')
    elif price and isinstance(price, float):
        return f'{price:.3f}'.replace('.', ' ')
    else:
        return f'{price}'
