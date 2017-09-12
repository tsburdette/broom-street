from actors import Actor, Item
import json

class Player(Actor):
    def __init__(self):
        #with open('game_data/items.json') as item_data:
        #   items = json.load(item_data)
        #   self.inventory = [Item(item_id, items[item_id]) for item_id in person_info['inventory']]
        self.description = "It's you!"
        self.inventory = []
        self.aliases = ['SELF', 'ME']

    def get_subactors(self):
        return self.inventory

    def get_description(self):
        # why does this call twice when inherited from actor?
        return self.description
