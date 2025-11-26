import json

class Player:
    def __init__(self, hp=100, hunger=50, thirst=50, money=20, inventory=None, stamina=100):
        self.hp = hp
        self.hunger = hunger
        self.thirst = thirst
        self.money = money
        self.inventory = inventory or []
        self.stamina = stamina

    def update_stat(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, max(0, getattr(self, stat) + value))

    def add_item(self, item):
        self.inventory.append(item)

    def save(self, filepath=None):
        # default to Lab3/data/player.json if no path
        filepath = filepath or 'Lab3/data/player.json'
        with open(filepath, 'w') as f:
            json.dump(self.__dict__, f)

    @classmethod
    def load(cls, filepath=None):
        filepath = filepath or 'Lab3/data/player.json'
        with open(filepath, 'r') as f:
            data = json.load(f)
        # If old save file missing stamina, default it
        if 'stamina' not in data:
            data['stamina'] = 100
        return cls(**data)