
#!/usr/local/bin/python
# -*- coding:utf-8 -*-

cars = 100
space_in_a_car = 4.0
drivers = 40.0 #40 will give an integer division
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#a comma will give a space here!
print "There are ", cars, " cars availble."
print "There are only ", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have ", passengers, "to carpool today."
print "We need to put about ", average_passengers_per_car, "in each car."
