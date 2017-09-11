import json

class Actor():
    def __init__(self, actor_id, actor_info):
        self.actor_id = actor_id
        self.name = actor_info['name']
        self.description = actor_info['description']
        with open('game_data/items.json') as item_data:
            items = json.load(item_data)
            self.inventory = [Item(item_id, items[item_id]) for item_id in actor_info['inventory']]
        try:
            self.aliases = actor_info['aliases']
        except KeyError:
            self.aliases = None

    def do_action(self, action, **kwargs):
        method = getattr(self, action.method.__name__, None)
        if method:
            method(**kwargs)

    def get_description(self):
        print(self.description or "\nThis thing is beyond description!\n")

    def fetch_dialogue(self):
        print("You would look awfully silly talking to this.")

    def remove_item(self, item_alias):
        for item in self.inventory:
            if item_alias in item.aliases:
                return item
        return None

class Room(Actor):
    def __init__(self, room_id, room_info):
        super().__init__(actor_id=room_id, actor_info=room_info)
        with open('game_data/people.json') as people_data:
            all_people = json.load(people_data)
            self.people = [Person(person_id, all_people[person_id])
                                for person_id in room_info['people']]
        self.exits = room_info['exits']
        self.aliases = ["ROOM", "HERE"]

    def __str__(self):
        # people should be a list of names in the room? Maybe return a person's idle sentence?
        people_format_string = '\n'.join(['{:}' for person in self.people])
        # exit formatting should return the direction, ex. 'Exits are: West, North, Door'
        exit_format_string = ', '.join(['{:}' for exit in self.exits.keys()])
        hyphen_string = "-----------------------------"
        return ("{}\n{}\n{}\n{}\n\n".format(hyphen_string,
                                      self.name,
                                      hyphen_string,
                                      self.description) + 
                people_format_string.format(*self.people) +
                "\nExits are: " + exit_format_string.format(*self.exits.keys()))

    def get_next_room(self, direction):
        return self.exits[direction]

    def get_subactors(self):
        return self.people + self.inventory

class Person(Actor):
    def __init__(self, person_id, person_info):
        super().__init__(actor_id=person_id, actor_info=person_info)
        self.idle_text = person_info['idle_text']

    def __str__(self):
        return "{} {}".format(self.name, self.idle_text)

    def get_description(self):
        return "{}, {}".format(self.name, self.description)

    def dialogue_mode(self):
        # Open dialog file for the given person
        dialogue_file_path = "game_data/dialogue/{}.json".format(self.actor_id)
        with open(dialogue_file_path) as dialogue_file:
            # Better way to do this than loading the person's entire dialogue?
            dialogue_tree = json.load(dialogue_file)
        # Should find a way to start at a new point if flag is set.
        dialogue_id = "START"
        while dialogue_id is not "END":
            # get dialogue_line from tree (graph?)
            dialogue_line = dialogue_tree[dialogue_id]
            # Print NPC dialogue first
            print("\n{name} says, \"{line}\"\n".format(
                name=self.name,
                line=dialogue_line["text"]))
            # Give all response options
            if dialogue_line["responses"]:
                for response_id, response in dialogue_line["responses"].items():
                    print("{response_id}. {response}".format(
                        response_id=response_id,
                        response=response["text"]))
                # Assume bad input
                is_valid_choice = False
                while not is_valid_choice:
                    # Get choice and check if valid
                    choice = input("\n> ")
                    if choice in dialogue_line["responses"].keys():
                        is_valid_choice = True
                        responses = dialogue_line["responses"]
                        chosen_line = responses[choice]
                        dialogue_id = chosen_line["id"]
                    else:
                        print("Invalid choice. Please choose again.")
            else:
                dialogue_id = "END"

    def get_subactors(self):
        return self.inventory

class Item(Actor):
    def __init__(self, item_id, item_info):
        super().__init__(actor_id=item_id, actor_info=item_info)

    def __str__(self):
        return self.name

    def get_description(self):
        return "{}: {}".format(self.name, self.description)

    def get_subactors(self):
        return []
