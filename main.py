import xml.etree.ElementTree as ElementTree


class GoTo:
    def __init__(self, text, key):
        self.text = text
        self.key = key


class Inventory:
    def __init__(self, items):
        self.items = items

    def manage(self):
        list_items = list(self.items.keys())
        list_items.sort()
        index = 1
        print("*** Inventory ***")
        for item in list_items:
            print(str(index) + " - " + item + " (" + str(self.items[item]) + ")")
            index += 1
        print("*****************")


class Place:
    def __init__(self, text, options, inventory):
        self.text = text
        self.options = options
        self.inventory = inventory

    def display(self):
        print(self.text)
        for k, v in self.options.items():
            print(k + " - " + v.text)
        print("i - Inventory")

    def get_next_place(self, key):
        if key == "i":
            self.inventory.manage()
            return self
        elif key == "q":
            exit(0)
        else:
            return self.options[key].key


class Interpreter:
    def __init__(self, places, first_place):
        self.places = places
        self.current_place = places[first_place]

    def run(self):
        while True:
            try:
                self.current_place.display()
                self.current_place = self.places[self.current_place.get_next_place(input())]
            except KeyError:
                pass


def parse_adventure(filename):
    root = ElementTree.parse(filename).getroot()
    start_place = root.attrib["start"]
    places = {}
    inventory = Inventory({"sword": 1, "gold coins": 50})
    for place in root:
        place_key = place.attrib["key"]
        place_description = place.find("description").text
        place_actions = {}
        for action in place.find("actions"):
            action_item = action.attrib["item"]
            action_description = action.attrib["description"]
            action_goto = action.attrib["goto"]
            place_actions[action_item] = GoTo(action_description, action_goto)
        places[place_key] = Place(place_description, place_actions, inventory)
    return Interpreter(places, start_place)


i = parse_adventure("adventure.xml")
i.run()
