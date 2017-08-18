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
