from room import Room

class Action():
    def __init__(self, method, **kwargs):
        self.method = method
        self.kwargs = kwargs

class GoAction(Action):
    def __init__(self, direction):
        super().__init__(method=Room.get_next_room, direction=direction)

class LookAction(Action):
    def __init__(self):
        super().__init__(method=Actor.get_description)
