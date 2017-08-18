class Actor():
    def do_action(self, action, **kwargs):
        method = getattr(self, action.method.__name__, None)
        if method:
            method(**kwargs)
