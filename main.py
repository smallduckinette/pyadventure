import xml.etree.ElementTree as ElementTree


class GoTo:
    def __init__(self, text, key):
        self.text = text
        self.key = key


class Place:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def display(self):
        print(self.text)
        for k, v in self.options.items():
            print(k + " - " + v.text)

    def get_next_place(self, key):
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
    for place in root:
        place_key = place.attrib["key"]
        place_description = place.find("description").text
        place_actions = {}
        for action in place.find("actions"):
            action_item = action.attrib["item"]
            action_description = action.attrib["description"]
            action_goto = action.attrib["goto"]
            place_actions[action_item] = GoTo(action_description, action_goto)
        places[place_key] = Place(place_description, place_actions)
    return Interpreter(places, start_place)


i = parse_adventure("adventure.xml")
i.run()
