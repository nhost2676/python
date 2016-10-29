name = 'Mark Olliver'
age = 17 #not a lie
height = 160 # cm
weight = 78 # kg
eys = 'Black'
teeth = 'White'
hair = 'Black'

print "Let talk about :%r" %name
print "He's %r centimets tall." %height
print "He's %r kg in weight." %weight
print "Actually that's not too heavy."
print "He got %r eyes and %r hair." % (eys, hair)
print "His teeth are usually %r depending on the coofe." %teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight,age + height + weight)