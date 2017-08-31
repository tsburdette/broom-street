from actor import Actor
from person import Person
from item import Item
import json

class Room(Actor):
    def __init__(self, room_id, room_info):
        self.room_id = room_id
        self.title = room_info['title']
        self.description = room_info['description']
        with open('people.json') as people_data:
            all_people = json.load(people_data)
            self.people = [Person(person_id, all_people[person_id])
                                for person_id in room_info['people']]
        with open('items.json') as item_data:
            items = json.load(item_data)
            self.inventory = [Item(item_id, items[item_id])
                                for item_id in room_info['inventory']]
        self.exits = room_info['exits']
        self.aliases = ["ROOM", "HERE"]

    def __str__(self):
        # people should be a list of names in the room? Maybe return a person's idle sentence?
        people_format_string = '\n'.join(['{:}' for person in self.people])
        # exit formatting should return the direction, ex. 'Exits are: West, North, Door'
        exit_format_string = ', '.join(['{:}' for exit in self.exits.keys()])
        hyphen_string = "-----------------------------"
        return ("{}\n{}\n{}\n{}\n\n".format(hyphen_string,
                                      self.title,
                                      hyphen_string,
                                      self.description) + 
                people_format_string.format(*self.people) +
                "\nExits are: " + exit_format_string.format(*self.exits.keys()))

    def get_next_room(self, direction):
        return self.exits[direction]

    def get_subactors(self):
        return self.people + self.inventory
