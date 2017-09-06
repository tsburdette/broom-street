class Actor():
    def do_action(self, action, **kwargs):
        method = getattr(self, action.method.__name__, None)
        if method:
            method(**kwargs)

    def get_description(self):
        print(self.description or "\nThis thing is beyond description!\n")

    def fetch_dialogue(self):
        print("You would look awfully silly talking to this.")
