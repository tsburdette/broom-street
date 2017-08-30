import json
from room import Room
from input_parser import ParsedLine

class Game:
    def __init__(self, seed_file, room_id):
        with open(seed_file) as data:
            self.world = json.load(data)
        self.current_room = Room(room_id, world[room_id])
        self.victory = False

    def change_room(direction):
        self.current_room = current_room.get_exit(direction)

def game_loop():
    game_state = Game('rooms.json', 'STREET')
    while True:
        print(game_state.room)
        action = input("\n> ")
        parsed_line = ParsedLine(action)

if __name__ == "__main__":
    game_loop()
