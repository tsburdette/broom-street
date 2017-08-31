from actor import Actor
import json

class Item(Actor):
    def __init__(self, item_id, item_info):
        self.item_id = item_id
        self.name = item_info['name']
        self.description = item_info['description']
        self.aliases = item_info['aliases']

    def __str__(self):
        return self.name

    def get_description(self):
        return "{}: {}".format(self.name, self.description)

    def get_subactors(self):
        return []
