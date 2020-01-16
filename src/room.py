# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, is_light):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.is_light = is_light

    def __str__(self):
        return f'\n{self.name}\n{self.description}\n'

    def print_items(self):
        for item in self.items:
            print(
                f'You see a {item.name}. It is {item.description}.')
