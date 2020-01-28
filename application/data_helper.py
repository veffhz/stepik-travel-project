import random


def random_limit(dictionary, quantity):
    if len(dictionary) < quantity:
        return random.sample(dictionary.items(), len(dictionary))
    return random.sample(dictionary.items(), quantity)
