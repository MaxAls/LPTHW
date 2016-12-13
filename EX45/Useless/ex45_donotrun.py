import sys



#################

class Game(object):

    def __init__(self):

        self.player = Player()

        self.levels = [
        Outside(),
        Entrance(),
        KeyRoom(),
        RiddleRoom(),
        SwordRoom(),
        BossRoom(),
        TreasureRoom()
        ]

        self.currentlevel = self.levels[1]

    def printWorld(self):

        self.currentlevel.describeYourself()

        for exit in self.levels:
            if exit is not self.currentlevel:
                print "In the far distance you see a %s. You could go there." % (exit.name)

    def getExit(self, exitname):
        for level in self.levels:
            if exitname == level.name:
                return level
        return None

    def start(self):
        print "Welcome to Hack-n-Slash."
        self.printWorld()
        userinput = raw_input("What do you do?> ")
        while (userinput != "quit") and (self.player.isAlive()):
            self.parseInput(userinput)
            if self.player.isAlive():
                userinput = raw_input("What do you do?> ")
        if not self.player.isAlive():
            print "You have died..."
        else:
            print "You give up on adventuring for today. Goodbye!"
        print "You had a score of %d" % self.player.score

    def parseInput(self, userinput):
        commands = userinput.split()
        if commands[0] == 'look':
            self.printWorld()
        elif commands[0] == 'go':
            newlevel = self.getExit(commands[1])
            if newlevel is not None:
                self.currentlevel = newlevel
                self.printWorld()
            else:
                print "There is no exit by that name."
        elif commands[0] == 'take':
            theitem = self.currentlevel.getItem(commands[1])
            if theitem is not None:
                self.player.takeItem(theitem)
                self.currentlevel.removeItem(theitem)
            else:
                print "There is no item by that name."
        elif commands[0] == 'attack':
            themonster = self.currentlevel.getMonster(commands[1])
            if themonster is not None:
                self.player.battle(themonster)
            else:
                print "There is no monster by that name"
        else:
            print """The available commands are:
                look            Look around you
                go X            Leave this level for exit X
                take Y          Take item Y
                attack Z        Attack monster Z
            """


#################

class Rooms(object):
    def __init__(self, roomname):
        self.name = roomname
        self.monsters = self.init_Monsters()
        self.items = self.init_Items()
        self.description = self.init_Description()

    def describe_Yourself(self):
        print self.description
        self.print_Monsters()
        self.print_Items()

    def init_Monsters(self):
        return []
    def init_Items(self):
        return []
    def init_Description(self):
        return ""

    def print_Monsters(self):
        for monster in self.monsters:
            monster.describe_Yourself()

    def print_Items(self):
        for item in self.items:
            item.describe_Yourself()

    def get_Monster(self, monstername):
        for monster in self.monsters:
            if monstername == monster.name:
                return monster
        return None

    def get_Item(self, itemname):
        for item in self.items:
            if itemname == item.name:
                return item
        return None

    def remove_Item(self, theitem):
        self.items.remove(theitem)

class Outside(Rooms):
    def initMonsters(self):
        return
        [
        none
        ]
    def initItems(self):
        return
        [
        Weapon('Large Hammer', 'is laying on the ground next to you', 50, 'smashes')
        ]
    def initDescription(self):
        return
        """
        You are standing in front of an old mansion.
        In front of you is a large, heavy looking door.
        What do you wish to do?
        """

class Entrance(Rooms):
    def initMonsters(self):
        return
        [
        none
        ]
    def initItems(self):
        return
        [
        none
        ]
    def initDescription(self):
        return
        """
        Upon opening the door you enter a room.
        A dim light comes from a lonely torch straight ahead.

        To your left you see a door that says: Brains

        To your right you see another that says: Brawns

        Which one do you wish to open?
        """

class KeyRoom(Rooms):
    def initMonsters(self):
        return
        [
        none
        ]
    def initItems(self):
        return
        [
        key
        book
        ]
    def initDescription(self):
        return
        """
        The door swings open, revealing a cozy little room.
        Straight ahead is a dusty bookshelf.
        To the right you spot two chairs around a table.
        And to the left is nothing but a worn out rug.
        Also, there is another door in the room
        What do you wish to do?
        """

class RiddleRoom(Rooms):
    def initMonsters(self):
        return
        [
        none
        ]
    def initItems(self):
        return
        [
        none
        ]
    def initDescription(self):
        return
        """
        You enter a pitch black room.
        You can't see a thing...
        The door you just passed through slams shut.
        You are locked in.
        What do you do?
        """

class SwordRoom(Rooms):
    def initMonsters(self):
        return
        [
        none
        ]
    def initItems(self):
        return
        [
        sword
        shield
        ]
    def initDescription(self):
        return
        """
        With loud creeking noise the door swings open.
        You stare into what appears to be an empty room.
        The only thing inside seems to be a golden sword hanging
        on the wall opposite to you.
        A door is to your left.
        What will your next action be?
        """

class BossRoom(Rooms):
    def initMonsters(self):
        return
        [
        Boss
        Skeleton
        Skeleton
        ]
    def initItems(self):
        return
        [
        none
        ]
    def initDescription(self):
        return
        """
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

class TreasureRoom(Rooms):
    def initMonsters(self):
        return
        [
        none
        ]
    def initItems(self):
        return
        [
        lots of Gold
        ]
    def initDescription(self):
        return
        """
        You enter the mysterious room that opened up behind the wall.
        You see a chest and open it. Inside you find heaps of Gold and a
        letter addressed to you personally! How mysterious... It reads:

        Dear player.

        I am filled with pride upon seing you alive and well. I realize
        you wanted to take a different path. You like action, thrills and
        adrenalin, and yet you had to think, evaluate and reflect.
        Yes I tricked you, but I am sure you have learned from the
        experience and you have been rewarded generously, haven't you?
        Well The door at the end of this room will lead to freedom.
        I wish you all the best.

        Sincerely,
        Yo' Momma
        """

#################

class Player(object):
    has:
    """
    health
    score
    Items
    """

    can do:
    """
    attackMonsters
    takeItem
    AddHealth
    AddScore
    BeAlive
    """

class Monster(object):
    def __init__(self, monstername, monsterdescription, attackverb,
                            attackstrength, starthealth, pointvalue):

        self.name = monstername
        self.description = monsterdescription
        self.verb = attackverb
        self.health = starthealth
        self.points = pointvalue
        self.strength = attackstrength

    def describeYourself(self):
        if self.isAlive():
            print "A %s is %s" % (self.name, self.description)
        else:
            print "The carcass of a %s lies on the ground." % self.name

    def isAlive(self):
        return self.health > 0

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 1:
            print "The %s falls!" % self.name

#################

class Item(object):
    def __init__(self, itemname, itemdescription):
        self.name = itemname
        self.description = itemdescription

    def describeYourself(self):
        print "A %s %s. You can take it" % (self.name, self.description)

    # Child classes should override this method to make changes to the player according with
    # what the item should change on the player
    def takenBy(self, player):
        pass

class Weapon(Item):
    def __init__(self, weaponname, weapondescription, attackstrength, attackverb):
        super(Weapon, self).__init__(weaponname, weapondescription)
        self.strength = attackstrength
        self.verb = attackverb

    def takenBy(self, player):
        player.changeWeapon(self)

class Food(Item):
    pass

#################
