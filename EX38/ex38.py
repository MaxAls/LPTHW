ten_things = "Apples Oranges Crows Telephone Light sugar"

print "wait there are not ten things in that list. let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now" % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # Whoa! Fancy
print stuff.pop()
print ' '.join(stuff) # What? cool!
print '#'.join(stuff[3:5]) # super stellar
