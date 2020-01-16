# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room(self):
        print('\nYour location:', self.current_room.name)
        print(self.current_room.description, '\n')
        for item in self.current_room.items:
            print(
                f"There's a {item.name} in this room. It is {item.description}.")

    def print_inventory(self):
        if not len(self.items):
            print('\nYour satchel is empty.')
        else:
            print('\nIn your satchel:')
            for item in self.items:
                print(f'{item.name}: {item.description}')

    def move_room(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print('\nAlas, you cannot move in that direction!')
        else:
            self.current_room = new_room
            self.print_current_room()

    def get(self, item_to_get, item_list):
        if any(item.name == item_to_get for item in self.current_room.items):
            self.items.append(item_list[item_to_get])
            self.current_room.items.remove(item_list[item_to_get])
            item_list[item_to_get].on_take()
        else:
            print(
                f"Hmm, doesn't look like there's a {item_to_get} in this room...")

    def drop(self, item_to_drop, item_list):
        if any(item.name == item_to_drop for item in self.items):
            self.items.remove(item_list[item_to_drop])
            self.current_room.items.append(item_list[item_to_drop])
            print(f'You drop the {item_to_drop} to the floor.')
        else:
            print(f"Pshh you don't even have a {item_to_drop}!")
