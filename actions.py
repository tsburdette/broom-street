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

class GetAction(Action):
    def __init__(self, args):
        match = re.match(r'(?P<item>.*)(?: FROM )(?(1)(?P<source>.*))', args) or re.match(r'(P<item>.+)', args)
        super().__init__(method=Game.get_item, item=match.group('item'),
                source=match.group('source') if len(match.groups()) > 1 else None)

class QuitAction(Action):
    def __init__(self, args):
        super().__init__(method=Game.quit)
