class GoTo:
    def __init__(self, text, key):
        self.text = text
        self.key = key


class Room:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def display(self):
        print(self.text)
        for k, v in self.options.items():
            print(k + " - " + v.text)

    def get_next_room(self, key):
        return self.options[key].key


class Interpreter:
    def __init__(self, rooms, first_room):
        self.rooms = rooms
        self.current_room = rooms[first_room]

    def run(self):
        while True:
            try:
                self.current_room.display()
                self.current_room = self.rooms[self.current_room.get_next_room(input())]
            except KeyError:
                pass


lake = Room("You are near a lake. The sky is blue, with just a few clouds. "
            "You can see on the other side of the lake a large castle. "
            "Closer to you, there is a dark forest.",
            {"1": GoTo("Go to the castle", "castle"), "2": GoTo("Enter the forest", "forest")})

forest = Room("The forest is deep and silent. You see a beautiful sword stuck in a tree, and you grab it.",
              {"1": GoTo("Go back to the lake", "lake")})

all_rooms = {"lake": lake, "forest": forest}

i = Interpreter(all_rooms, "lake")
i.run()
