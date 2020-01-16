# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room(self):
        print(self.current_room)
        self.current_room.print_items()

    def print_inventory(self):
        if not len(self.items):
            print('\nYour satchel is empty.')
        else:
            print('\nIn your satchel:')
            for item in self.items:
                print(item)

    def move_room(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print('\nAlas, you cannot move in that direction!')
        else:
            self.current_room = new_room
            self.print_current_room()

    def get(self, item_to_get):
        if any(item.name == item_to_get for item in self.current_room.items):
            item_obj = next(
                (item for item in self.current_room.items if item.name == item_to_get), None)
            self.items.append(item_obj)
            self.current_room.items.remove(item_obj)
            item_obj.on_take()
        else:
            print(
                f"Hmm, doesn't look like there's a {item_to_get} in this room...")

    def drop(self, item_to_drop):
        if any(item.name == item_to_drop for item in self.items):
            item_obj = next(
                (item for item in self.items if item.name == item_to_drop), None)
            self.items.remove(item_obj)
            self.current_room.items.append(item_obj)
            item_obj.on_drop()
        else:
            print(f"Pshh you don't even have a {item_to_drop}!")
