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
