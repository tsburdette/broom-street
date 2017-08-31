from actor import Actor
from item import Item
import json

class Person(Actor):
    def __init__(self, person_id, person_info):
        self.person_id = person_id
        self.name = person_info['name']
        self.idle_text = person_info['idle_text']
        self.description = person_info['description']
        with open('items.json') as item_data:
            items = json.load(item_data)
            self.inventory = [Item(item_id, items[item_id]) for item_id in person_info['inventory']]
        self.aliases = person_info['aliases']

    def __str__(self):
        return "{} {}".format(self.name, self.idle_text)

    def get_description(self):
        return "{}, {}".format(self.name, self.description)

    def get_subactors(self):
        return self.inventory
