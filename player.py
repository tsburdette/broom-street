from actor import Actor
from item import Item
import json

class Player(Actor):
    def __init__(self):
        self.name = player_info['name']
        self.description = player_info['description']
        with open('game_data/items.json') as item_data:
           items = json.load(item_data)
           self.inventory = [Item(item_id, items[item_id]) for item_id in person_info['inventory']]
        self.aliases = ['SELF', 'ME']
