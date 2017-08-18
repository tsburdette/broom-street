import json
from room import Room

room_id = 'STREET'
world = {}

def game_setup():
    # setup initial room/vars
    with open('rooms.json') as rooms:
        global world
        world = json.load(rooms)
    game_loop()

def game_loop():
    while True:
        current_room = Room(room_id, world[room_id])
        print(current_room)
        action = input("\n> ")
        if action in ["WEST", "EAST"]:
            global room_id
            room_id = current_room.get_next_room(action)
        else:
            print("That is not a valid action.\n")

if __name__ == "__main__":
    game_setup()
