name = 'Max Alsleben'
age = 20 # Also not a lie
height = 73 # inches
weight = 165 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'
height_in_cm = height * 2.54
weight_in_kg = weight * 0.45359237


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d punds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line was tricky, but I got it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight
)
print "His Height converted to centimeters is %d" % height_in_cm
print "His weight converted to kilograms is %d" % weight_in_kg
