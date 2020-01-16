# Write a class to hold player information, e.g. what room they are in
# currently.

from item import LightSource


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))


def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room(self):
        if self.current_room.is_light or self.has_light():
            prLightPurple(self.current_room)
            self.current_room.print_items()
        else:
            print('')
            prLightPurple(self.current_room.name)
            prLightPurple("It's pitch black!")

    def print_inventory(self):
        if not len(self.items):
            prGreen('\nYour satchel is empty.')
        else:
            prGreen('\nIn your satchel:')
            for item in self.items:
                prGreen(item)

    def move_room(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            prRed('\nAlas, you cannot move in that direction!')
        else:
            self.current_room = new_room

    def get(self, item_to_get):
        if self.current_room.is_light or self.has_light():
            if any(item.name == item_to_get for item in self.current_room.items):
                item_obj = next(
                    (item for item in self.current_room.items if item.name == item_to_get), None)
                self.items.append(item_obj)
                self.current_room.items.remove(item_obj)
                item_obj.on_take()
            else:
                prLightPurple(
                    f"Hmm, doesn't look like there's a {item_to_get} in this room...")
        else:
            print('Good luck finding that in the dark!')

    def drop(self, item_to_drop):
        if any(item.name == item_to_drop for item in self.items):
            item_obj = next(
                (item for item in self.items if item.name == item_to_drop), None)
            self.items.remove(item_obj)
            self.current_room.items.append(item_obj)
            item_obj.on_drop()
        else:
            print(f"Pshh you don't even have a {item_to_drop}!")

    def has_light(self):
        return any(isinstance(item, LightSource) for item in self.items)
