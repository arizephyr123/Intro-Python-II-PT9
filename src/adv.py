import sys

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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
game_started = False
name = "Player"
def start_game():
    global name
    name = input("Welcome to the Game! Enter your avatar's name:\n")

    global game_started
    game_started = True
    return name

start_game()

player = Player('outside', name)

valid_directions = ["n", "e", "s", 'w']

while game_started == True:
    curr_room = player.curr_loc
    cmd = input(f"{player.name}, your current location is {curr_room}.\n{room[curr_room].description} Which direction would you like to go next?\n")

    if len(cmd.split()) == 1:
        if cmd[0].lower() in valid_directions:
            print(cmd, cmd[0].lower())
        elif cmd[0].lower() == 'q':
            print("\nGoodbye")
            sys.exit()
        else:
            print(f"{cmd.capitalize()} is not a valid direction. Try North, South, East, or West")

    else: 
        print(cmd.split())


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
