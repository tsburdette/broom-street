import actions

class InputParser:
    self.actions = {
            "GO" : actions.GoAction,
            "LOOK" : actions.LookAction
            }

    def get_action(self, input_string):
        self.args = input_string.upper().split(' ', 1)
        if self.args[0] in self.actions.keys():
            try:
                return (self.actions[self.args[0]](self.args[1])
                        if len(self.args) > 1
                        or self.actions[self.args[0]]())
            except TypeError as e:
                raise

class ParsedLine:
    self.action_list = {
            "GO" : actions.GoAction,
            "LOOK" : actions.LookAction
            }

    def __init__(self, input_string):
        args = input_string.upper().split(' ', 1)
        if args[0] in self.action_list.keys():
            self.action = self.action_list(args[0])
