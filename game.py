import json
from input_parser import ParsedLine
from game_state import Game

def game_loop():
    game_state = Game('rooms.json', 'STREET')
    while True:
        print(game_state.current_room)
        action = input("\n> ")
        try:
            parsed_line = ParsedLine(action)
            game_state.do_action(parsed_line.action)
        except:
            print("Cannot do that.")

if __name__ == "__main__":
    game_loop()
