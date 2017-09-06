from game_state import Game
import re

class Action():
    def __init__(self, method, **kwargs):
        self.method = method
        self.kwargs = kwargs

class GoAction(Action):
    def __init__(self, direction):
        super().__init__(method=Game.change_room, direction=direction)

class LookAction(Action):
    def __init__(self, target):
        super().__init__(method=Game.print_look, target=target)

class TalkAction(Action):
    def __init__(self, target):
        target_match = re.match(r'(?:TO )?([\w ]+)', target).group(1)
        super().__init__(method=Game.initiate_dialogue, target=target_match)
