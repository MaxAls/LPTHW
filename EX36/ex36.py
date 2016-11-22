from sys import exit
import wave

global secret_door
secret_door = False
global found_sword
found_sword = False
global found_shield
found_shield = False
#Fanfare = wave.open(/Users/Maximilian/Repositories/LPTHW/EX36/Fanfare.wav/)

def start():
    print """
    You are standing in front of an old mansion.
    In front of you is a large, heavy looking door.
    What do you wish to do?
    """

    choice = raw_input("> ")

    if "door" in choice:
        first_room()
    elif "sneak" in choice:
        final_room()

    else:
        print """
        Let's try that again
        """
        start()


def first_room():
    print """
    Upon opening the door you enter a room.
    A dim light comes from a lonely torch straight ahead.

    To your left you see a door that says: Brains

    To your right you see another that says: Brawns

    Which one do you wish to open?
    """

    choice = raw_input("> ")

    if "left" in choice:
        key_room()
    elif "right" in choice:
        sword_room()
    else:
        print """
        This narrator is getting tired of your indecisiveness.
        """
        first_room()

def key_room():
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
            stone_room()
        else:
            print """
            I know, lot's of things to look at here.
            Let me tell you again what you can find here.
            """
            key_room()


def sword_room():
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
            #Fanfare
            print """
            DUDUDUDUUUUN
            Link... uh.... YOU have obtained a sword!
            """
            found_sword = True
        elif "look" in choice:
            print """
            You spot something behind the open door.
            It is a shield!
            How terribly dumb had it been if you had overlooked that.
            """

            choice = raw_input("> ")

            if "shield" in choice:
                #Fanfare
                print """
                DUDUDUDUUUUN
                Link... uh.... YOU have obtained a shield!
                """
                found_shield = True
            else:
                print """
                Well, It's your choice
                """
        elif "door" in choice:
            boss_room()
        else:
            print """
            Well, It's your choice...
            """

def stone_room():
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
                secret_door = True
                final_room()
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


def boss_room():
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

    print """
    Hint: You can now hit and block
    """

    #def health(monster_health, my_health):
        #print "The monsters health: %d" % monster_health
        #print "Your health: %d" % my_health

    #def monster_hit():
        #print """
        #The creature takes a terrifying swing.
        #"""
        #return my_health - 50

    #def hit_nosword():
        #print """
        #You hit the creature with your fist.
        #Why would you do that.
        #"""
        #return monster_health - 10

   #def hit_sword():
        #print """
        #You hit the creature with your Sword.
        #You deal some massive damage!
        #"""
        #return monster_health - 100

    #def blocknoshield():
        #print """
        #You try to block the creatures hit with your bare arm.
        #Somehow I feel like that is not going to do you any good.
        #"""
        #return monster_hit()

    #def blockshield():
        #print """
        #You raise your shield and block the creatures hit.
        #No harm done.
        #"""
        #return not monster_hit()


    monster_health = 200
    my_health = 150

    while monster_health > 0:

        choice = raw_input("> ")

        if choice == "hit" and found_sword:
            print """
            The golden sword unleashes its power and distroys the creature!
            """
            final_room()

        elif choice == "hit" and not found_sword:
            dead("Why would you even try this with your bare hands?")
            #monster_hit()
            #hit_nosword()
            #print "The creatures health:", monster_health
            #print "Your health:", my_health

        elif choice == "block" and found_shield:
            print """
            You block the creatures hit and remain unharmed!
            """
            #monster_hit()
            #blockshield()
            #print "The creatures health:", monster_health
            #print "Your health:", my_health

        elif choice == "block" and not found_shield:
            dead("You get slashed into bits and pieces trying to block this hit")
            #monster_hit()
            #blocknoshield()
            #print "The creatures health:", monster_health
            #print "Your health:", my_health
        #elif monster_health < 0:
            #print "You win!"
            #final_room()
        else:
            print """
            The creature jumps at you with terrifying speed.
            You move too slow, it tears you appart in seconds and devours
            your flesh
            """
            dead("Death due to missing reflexes")


def final_room():
    gold = False

    if secret_door:
        print """
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
        gold = True
        print "Do you have gold?", gold
        exit(0)

    elif found_sword:
        print """
        After this massive fight you are overjoyed to find an unlocked door
        behind a giant pile of wrotten flesh and bones. You pass through it
        and find yourself in a room with a lonley chest. Inside the
        chest you find heaps of Gold and a letter addressed
        to you personally! How mysterious... It reads:

        Dear player.

        I am filled with pride upon seing you alive and well. I realize
        you wanted to take a different path. You like puzzles, riddles,
        and generally using your brain. Yet you had to explore and fight
        to the death. Yes I tricked you, but I am sure you have learned
        from the experience and you have been rewarded generously,
        haven't you?
        Well The door at the end of this room will lead to freedom.
        I wish you all the best.

        Sincerely,
        Yo' Momma
        """
        gold = True
        print "Do you have gold?", gold
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

        gold = False
        print "Do you have gold?", gold
        exit(0)


def dead(why):
    print why
    exit(0)

start()
