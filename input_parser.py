import actions

class ParsedLine:
    action_list = {
            "GO" : actions.GoAction,
            "LOOK" : actions.LookAction,
            "TALK" : actions.TalkAction,
#            "GET" : actions.GetAction,
#            "HELP" : actions.HelpAction,
            "QUIT" : actions.QuitAction
            }

    def __init__(self, input_string):
        split_line = input_string.upper().split(' ', 1)
        action_name = split_line[0]
        args = split_line[1].rstrip() if len(split_line) > 1 else ""
        if action_name in self.action_list.keys():
            self.action = self.action_list[action_name](args)
