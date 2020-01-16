from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('PlayerOne', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

item = {'sword': Item('sword', 'your standard sword'),
        'iPhone': Item('iPhone', 'an iPhoneX')}

room['outside'].items.append(item['sword'])
room['outside'].items.append(item['iPhone'])


def main():
    print_welcome_message()
    game_action()


def game_action():
    print_current_room()
    input_player_action()


def print_welcome_message():
    welcome_message = '\n** Welcome to Adventure Game! **'
    print(welcome_message)


def print_current_room():
    print('\nYour location:', player.current_room.name)
    print(player.current_room.description, '\n')
    for item in player.current_room.items:
        print(
            f"There's a {item.name} in this room. It is {item.description}.")


def print_options():
    print('n: go North')
    print('s: go South')
    print('e: go East')
    print('w: go West')
    print('l: check location')
    print('i: check inventory')
    print('get/take [item]: pick up item')
    print('drop [item]: drop item')
    print('q: quit game')
    input_player_action()


def input_player_action():
    input_message = '\nWhat would you like to do? [press o to see your options] '

    key = input(input_message).split(' ')
    check_input(key)


def check_input(input):
    if len(input) == 1:
        key = input[0]

        cardinal_directions = {'n': 'North',
                               's': 'South',
                               'e': 'East',
                               'w': 'West'}

        if key == 'q':
            quit_game()
        elif key == 'o':
            print_options()
        elif key == 'l':
            game_action()
        elif key == 'i' or key == 'inventory':
            print_inventory()
            input_player_action()
        elif key in cardinal_directions.keys():
            print(f'You move {cardinal_directions[key]}.')
            move_room(key)
            game_action()
        else:
            bad_input()
    elif len(input) == 2:
        if input[0] == 'get' or input[0] == 'take':
            get(input[1])
        elif input[0] == 'drop':
            drop(input[1])
        else:
            bad_input()
    else:
        bad_input()


def bad_input():
    print("Eww gross, you can't do that in here!")
    input_player_action()


def move_room(direction):
    direction_link = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
    new_room = getattr(player.current_room, direction_link[direction])

    if not new_room:
        print('Alas, you cannot move in that direction!\n')
    else:
        player.current_room = new_room


def print_inventory():
    if not len(player.items):
        print('\nYour satchel is empty.\n')
    else:
        print('In your satchel:')
        for item in player.items:
            print(f'{item.name}: {item.description}')
        print('\n')


def get(item_to_get):
    if any(item.name == item_to_get for item in player.current_room.items):
        player.items.append(item[item_to_get])
        player.current_room.items.remove(item[item_to_get])
        print(f'Sweet! You now has {item_to_get}!')
    else:
        print(
            f"Hmm, doesn't look like there's a {item_to_get} in this room...")
    input_player_action()


def drop(item_to_drop):
    if any(item.name == item_to_drop for item in player.items):
        player.items.remove(item[item_to_drop])
        player.current_room.items.append(item[item_to_drop])
        print(f'You drop the {item_to_drop} to the floor.')
    else:
        print(f"Pshh you don't even have a {item_to_drop}!")
    input_player_action()


def quit_game():
    print('\nWhat? Leaving so soon? Ok fine, BYEEEE.')


main()
