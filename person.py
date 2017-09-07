from actor import Actor
from item import Item
import json

class Person(Actor):
    def __init__(self, person_id, person_info):
        self.person_id = person_id
        self.name = person_info['name']
        self.idle_text = person_info['idle_text']
        self.description = person_info['description']
        with open('items.json') as item_data:
            items = json.load(item_data)
            self.inventory = [Item(item_id, items[item_id]) for item_id in person_info['inventory']]
        self.aliases = person_info['aliases']

    def __str__(self):
        return "{} {}".format(self.name, self.idle_text)

    def get_description(self):
        return "{}, {}".format(self.name, self.description)

    def dialogue_mode(self):
        # Open dialog file for the given person
        dialogue_file_path = "./dialogue/{}.json".format(self.person_id)
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
