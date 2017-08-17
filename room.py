class Room():
    def __init__(self, room_id, room_info):
        self.room_id = room_id
        self.title = room_info['title']
        self.description = room_info['description']
        self.people = room_info['people']
        self.objects = room_info['objects']
        self.exits = room_info['exits']

    def __str__(self):
        # people should be a list of names in the room? Maybe return a person's idle sentence?
        people_format_string = '\n'.join(['{:}' for person in self.people])
        # exit formatting should return the direction, ex. 'Exits are: West, North, Door'
        exit_format_string = ', '.join(['{:}' for exit in self.exits.keys()])
        return ("{}\n{}\n".format(self.title, self.description) + 
                people_format_string.format(*self.people) +
                "\nExits are: " + exit_format_string.format(*self.exits.keys()))

    def get_next_room(self, direction):
        return self.exits[direction]
