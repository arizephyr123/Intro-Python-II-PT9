# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, curr_loc, name):
        self.name = name
        self.curr_loc = curr_loc

    def __str__(self):
        return f'Player: {self.name} -> location: {self.curr_loc}'