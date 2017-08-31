import actions

class ParsedLine:
    action_list = {
            "GO" : actions.GoAction,
            "LOOK" : actions.LookAction
            }

    def __init__(self, input_string):
        action_name, args = input_string.upper().split(' ', 1)
        if action_name in self.action_list.keys():
            self.action = self.action_list[action_name](args)
