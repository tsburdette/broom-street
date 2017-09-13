import json
import sys
from queue import Queue
from actors import Room
from player import Player

class Game:
    def __init__(self, seed_file, room_id):
        with open(seed_file) as data:
            self.world = json.load(data)
        self.current_room = Room(room_id, self.world[room_id])
        self.player = Player()
        self.victory = False

    def change_room(self, arg_dict):
        direction = arg_dict['direction']
        try:
            new_room_id = self.current_room.get_next_room(direction)
            self.current_room = Room(new_room_id, self.world[new_room_id])
        except:
            print("Can't go {}.\n".format(arg_dict['direction']))

    def print_look(self, arg_dict):
        target_alias = arg_dict['target']
        try:
            target = self.find_target(target_alias)
            print('{}\n'.format(target.get_description()))
        except:
            print("Can't find {}.\n".format(target_alias))

    def initiate_dialogue(self, arg_dict):
        target_alias = arg_dict['target']
#        try:
        target = self.find_target(target_alias)
        target.dialogue_mode()
#        except:
#            print("Can't find {}.\n".format(target_alias))

    def get_item(self, arg_dict):
        source_alias = arg_dict['source'] or 'HERE'
        item_alias = arg_dict['target']
        source = self.find_target(source_alias)
        self.player.add_item(source.remove_item(item_alias))

    def put_item(self, arg_dict):
        destination_alias = arg_dict['destination'] or 'HERE'
        item_alias = arg_dict['target']
        destination = self.find_target(destination_alias)
        destination.add_item(self.player.remove_item(item_alias))

    def find_target(self, target_alias):
        target_queue = Queue()
        target_queue.put(self.player)
        target_queue.put(self.current_room)
        while not target_queue.empty():
            possible_match = target_queue.get()
            if target_alias in possible_match.aliases:
                return possible_match
            else:
                for sub_item in possible_match.get_subactors():
                    target_queue.put(sub_item)

    def quit(self, args):
        sys.exit()

    def do_action(self, action):
        method = getattr(self, action.method.__name__, None)
        if method:
            method(action.kwargs)
