class Player(object):

    Items = {}

#    def __init__(self):
#        self.weapon = Weapon('bare hands', '', 1, "scratch and slap")
#        self.health = 100
#        self.score = 0
#
#    def takeItem(self, theitem):
#        theitem.takenBy(self)
#
#    def changeWeapon(self, wp):
#        print "You take the %s into your hands." % wp.name
#        self.weapon = wp
#
#    def addHealth(self, amount):
#        newhealth = min(self.health + amount, 100)
#        print "Your heath is boosted from %d to %d" % (self.health, newhealth)
#        self.health = newhealth
#
#    def addScore(self, amount):
#
#        self.score += amount
#
#    def isAlive(self):
#        return self.health > 0
#
#    def battle(self, monster):
#
#        while monster.isAlive() and self.isAlive():
#            damagedone = self.weapon.strength
#            damagereceived = monster.strength
#            print "You %s the %s with your %s!!" % (self.weapon.verb, monster.name, self.weapon.name)
#            print "%s takes %d damage." % (monster.name, damagedone)
#            monster.takeDamage(damagedone)
#
#            if monster.isAlive():
#                print "The %s %s you!" % (monster.name, monster.verb)
#                print "You take %d damage." % damagereceived
#                self.health -= damagereceived
#
#            else:
#                print "You get %d points!" % monster.points
#                self.addScore(monster.points)
#
#
#lass Monster(object):
#    def __init__(self, monstername, monsterdescription, attackverb,
#                            attackstrength, starthealth, pointvalue):
#
#        self.name = monstername
#        self.description = monsterdescription
#        self.verb = attackverb
#        self.health = starthealth
#        self.points = pointvalue
#        self.strength = attackstrength
#
#    def describeYourself(self):
#        if self.isAlive():
#            print "A %s is %s" % (self.name, self.description)
#        else:
#            print "The carcass of a %s lies on the ground." % self.name
#
#    def isAlive(self):
#        return self.health > 0
#
#    def takeDamage(self, damage):
#        self.health -= damage
#        if self.health < 1:
#            print "The %s falls!" % self.name
##
