from Characters import *

class Rooms(object):

    def enter(self):
        pass

class Outside(Rooms):

    def enter(self):
        print """
        You are standing in front of an old mansion.
        In front of you is a large, heavy looking door.
        What do you wish to do?
        """

        choice = raw_input("> ")

        if "door" in choice:
            return 'Entrance'
        elif "sneak" in choice:
            return 'Treasure_Room'

        else:
            print """
            Let's try that again
            """
            return 'Outside'

class Entrance(Rooms):

    def enter(self):
        print """
        Upon opening the door you enter a room.
        A dim light comes from a lonely torch straight ahead.

        To your left you see a door that says: Brains

        To your right you see another that says: Brawns

        Which one do you wish to open?
        """

        choice = raw_input("> ")

        if "left" in choice:
            return 'Key_Room'
        elif "right" in choice:
            return 'Sword_Room'
        else:
            print """
            This narrator is getting tired of your indecisiveness.
            """
            return 'Entrance'

class KeyRoom(Rooms):

    def enter(self):
        print """
        The door swings open, revealing a cozy little room.
        Straight ahead is a dusty bookshelf.
        To the right you spot two chairs around a table.
        And to the left is nothing but a worn out rug.
        Also, there is another door in the room
        What do you wish to do?
        """
        found_key = False

        while True:

            choice = raw_input("> ")

            if "rug" in choice and not found_key:
                print """
                You get closer to the rug
                It looks as though something is laying underneath it.
                """

                choice = raw_input("> ")

                if "flip" or "turn" or "over" or "look" or "under" in choice:
                    print """
                    Now would you look at that! You found a key! Great!
                    """
                    found_key = True

                else:
                    print """
                    Let's try that again
                    """

            elif "bookshelf" in choice:
                print """
                You look throught the books, but find nothing
                """

            elif "Table" in choice:
                print """
                Well, it was worth a shot, but there's nothing there.
                """

            elif "door" in choice and not found_key:
                print """
                the door is locked
                """

            elif "door" in choice and found_key:
                print """
                Congratulations. You have solved the first riddle!
                """
                return 'Riddle_Room'

            else:
                print """
                I know, lot's of things to look at here.
                Let me tell you again what you can find here.
                """
                return 'Key_Room'


class RiddleRoom(Rooms):

    def enter(self):
        print """
        You enter a pitch black room.
        You can't see a thing...
        The door you just passed through slams shut.
        You are locked in.
        What do you do?
        """
        global secret_door

        choice = raw_input("> ")

        if "wall" in choice:

            while True:

                print """
                You touch the wall.
                You feel the wall.
                You are the... wait no.
                But you do find some lose stones on the right hand wall.
                There appear to be 3 lose stones in total, all next to each other.
                Furthermore it seems they can be pushed! #How original...
                In what order do you want to press them?
                """

                choice1 = int(raw_input("> "))
                choice2 = int(raw_input("> "))
                choice3 = int(raw_input("> "))

                if ((choice1 == 2) and (choice2 == 1) and (choice3 == 3)):
                    print """
                    Light floods the room.
                    A section of the wall slides outwards and to the right.
                    You have revealed a secret passageway to another room!
                    """
                    Player.Items['Secret_Passage'] = 'Not actually an Item'
                    return 'Treasure_Room'

                else:
                    print """
                    Nothing happens. Try again.
                    """

        else:
            print """
            you stumble around the room searching desperately for a way out.
            The door doesn't budge.
            You grow weaker and weaker over the next few days
            until you eventually die of thirst and starvation,
            cowered into a corner like the pathetic dimwit you are.
            """
            dead("Death due to Idiocy")


class SwordRoom(Rooms):

    def enter(self):
        print """
        With loud creeking noise the door swings open.
        You stare into what appears to be an empty room.
        The only thing inside seems to be a golden sword hanging
        on the wall opposite to you.
        A door is to your left.
        What will your next action be?
        """
        global found_sword
        global found_shield

        while True:

            choice = raw_input("> ")

            if "sword" in choice:
                print """
                DUDUDUDUUUUN
                Link... uh.... YOU have obtained a sword!
                """
                Player.Items['Sword'] = 'Golden'
                print Player.Items

            elif "look" in choice:
                print """
                You spot something behind the open door.
                It is a shield!
                How terribly dumb had it been if you had overlooked that.
                """

                choice = raw_input("> ")

                if "shield" in choice:
                    print """
                    DUDUDUDUUUUN
                    Link... uh.... YOU have obtained a shield!
                    """
                    Player.Items['Shield'] = 'Unbreakable'
                    print Player.Items

                else:
                    print """
                    Well, It's your choice
                    """

            elif "door" in choice:
                return 'Boss_Room'

            else:
                print """
                Well, It's your choice...
                """

class BossRoom(Rooms):

    def enter(self):
        print """
        As you open the door, the smell of rotting corpses hits you like a wall.
        It really doesn't seem like a good idea to go inside anymore.
        Nevertheless you do not get discouraged!
        You pass through the door and stand inside a filthy room.
        In the middle of which stands a creature the likes of which you have
        never seen before.
        It is human, yet entirely inhuman. It has no face, merely a mouth.
        Its jaw is lined with what looks like hundreds of needles.
        It is hunched over, its huge hands sliding along the floor.

        It spots you, turns its head slightly and presents the most gruesome
        grin you have ever seen.

        As you stand in utter shock, the door behind you slams shut.
        There is no way out.

        You have no choice. It is time to fight.
        """

        monster_health = 200
        my_health = 150

        while monster_health > 0:

            choice = raw_input("> ")

            if choice == "hit" and 'Sword' in Player.Items:
                print """
                The golden sword unleashes its power and distroys the creature!
                """
                return 'Treasure_Room'

            elif choice == "hit" and not 'Sword' in Player.Items:
                dead("Why would you even try this with your bare hands?")

            elif choice == "block" and 'Shield' in Player.Items:
                print """
                You block the creatures hit and remain unharmed!
                """

            elif choice == "block" and not 'Shield' in Player.Items:
                dead("You get slashed into bits and pieces trying to block this hit")

            else:
                print """
                The creature jumps at you with terrifying speed.
                You move too slow, it tears you appart in seconds and devours
                your flesh
                """
                dead("Death due to missing reflexes")

class TreasureRoom(Rooms):

    def enter(self):

        if 'Secret_Passage' in Player.Items:
            print """
            You enter the mysterious room that opened up behind the wall.
            You see a chest and open it. Inside you find heaps of Gold and a
            letter addressed to you personally! How mysterious... It reads:

            Dear player.

            I am filled with pride upon seing you alive and well. I am sure you
            have learned from the experience and you have been
            rewarded generously, haven't you?
            Well The door at the end of this room will lead to freedom.
            I wish you all the best.

            Sincerely,
            Yo' Momma
            """

            Player.Items['Gold'] = 'Heaps'
            print Player.Items

            exit(0)


        elif 'Sword' in Player.Items:
            print """
            After this massive fight you are overjoyed to find an unlocked door
            behind a giant pile of wrotten flesh and bones. You pass through it
            and find yourself in a room with a lonley chest. Inside the
            chest you find heaps of Gold and a letter addressed
            to you personally! How mysterious... It reads:

            Dear player.

            I am filled with pride upon seing you alive and well. I am sure you
            have learned from the experience and have
            been rewarded generously, haven't you?
            Well The door at the end of this room will lead to freedom.
            I wish you all the best.

            Sincerely,
            Yo' Momma
            """

            Player.Items['Gold'] = 'Heaps'
            print Player.Items['Gold']

            exit(0)


        else:
            print """
            After a short distance around the building you find yourself at the
            back entrance. You try to open the door. It is unlocked.
            You enter and find a room filled with nothing but a chest.
            Inside the chest you find heaps of Gold and a letter addressed
            to you personally! How mysterious... It reads:

            Dear player.

            Good Job, you found the last room! How very smart of you.
            Yet you did it without any effort. So you won't be receiveing
            any gold.
            Sorry.

            Sincerely,
            Yo' Momma
            """

            Player.Items['Gold'] = 'Cheaters get nothing'
            print Player.Items

            exit(0)


class Map(object):

    rooms = {
            'Outside': Outside(),
            'Entrance': Entrance(),
            'Key_Room': KeyRoom(),
            'Riddle_Room': RiddleRoom(),
            'Sword_Room': SwordRoom(),
            'Boss_Room': BossRoom(),
            'Treasure_Room': TreasureRoom()
            }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)
