import json

def save_game(filepath, data):
    # Path compatibility for Lab3
    if not filepath.startswith('Lab3/'):
        filepath = 'Lab3/' + filepath if not filepath.startswith('data/') else 'Lab3/' + filepath
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_game(filepath):
    if not filepath.startswith('Lab3/'):
        filepath = 'Lab3/' + filepath if not filepath.startswith('data/') else 'Lab3/' + filepath
    with open(filepath, 'r') as f:
        return json.load(f)

def random_chance(chance):
    from random import randint
    return randint(1, 100) <= chance