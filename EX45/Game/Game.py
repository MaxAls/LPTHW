from sys import exit
from Rooms import *
from Characters import *

##################################

class Engine(object):
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):

        print """
        To interact, use the names of the things You want to interact with
        """

        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('Treasure_Room')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)


        current_room.enter()

def dead(why):
    print why
    exit(0)

##################################

a_map = Map('Outside')
a_game = Engine(a_map)
a_game.play()

Outside()
