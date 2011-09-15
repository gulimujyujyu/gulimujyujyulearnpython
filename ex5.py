
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
my_name = 'Gulimujyujyu'
my_age = 23 # not a lie
my_height = 170 # cm
my_weight = 53 # kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d pounds heavy. " %my_weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %(my_teeth)

#this line is tricky, try to get it exactly right. Brackets have such quality.
print "If I add %d, %d, and %d I get %r" % (
    my_age, my_height, my_weight, my_age+my_height+my_weight)
