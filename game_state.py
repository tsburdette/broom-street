import json
from queue import Queue
from room import Room

class Game:
    def __init__(self, seed_file, room_id):
        with open(seed_file) as data:
            self.world = json.load(data)
        self.current_room = Room(room_id, self.world[room_id])
        self.victory = False

    def change_room(self, arg_dict):
        direction = arg_dict['direction']
        new_room_id = self.current_room.get_next_room(direction)
        self.current_room = Room(new_room_id, self.world[new_room_id])

    def print_look(self, arg_dict):
        target_alias = arg_dict['target']
        target = self.find_target(target_alias)
        print(target.get_description())

    def find_target(self, target_alias):
        target_queue = Queue()
        target_queue.put(self.current_room)
        while not target_queue.empty():
            possible_match = target_queue.get()
            if target_alias in possible_match.aliases:
                return possible_match
            else:
                for sub_item in possible_match.get_subactors():
                    target_queue.put(sub_item)

    def do_action(self, action):
        method = getattr(self, action.method.__name__, None)
        if method:
            method(action.kwargs)
