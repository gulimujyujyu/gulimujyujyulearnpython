
#!/usr/local/bin/python
# -*- coding:utf-8 -*-

##Animal is-a object.
class Animal(object):
	pass

##Dog is-a Animal	
class Dog(Animal):
	def __init__(self, name):
		##Dog has-a name
		self.name = name
	
##Cat is-a Animal	
class Cat(Animal):
	def __init__(self, name):
		##Cat has-a name
		self.name = name

##Person is-a Animal		
class Person(Animal):
	def __init__(self, name):
		##Person has-a name
		self.name = name
		##Person has-a pet
		self.pet = None
		
##Employee is-a Person
class Employee(Person):
	def __init__(self, name, salary):
		##Employee is-a Person
		super(Employee, self).__init__(name)
		##Employee has-a salary
		self.salary = salary

##Fish is-a object
class Fish(object):
	pass
	
##Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	
##Rover is a dog
rover = Dog("Rover")
##Satan is a cat
satan = Cat("Cat")
##mary is a person
mary = Person("Mary")
mary.pet = satan
##Frank is an employee
frank = Employee("Frank", 120000)
frank.pet = rover
##Flipper is a fish
flipper = Fish()
##crouse is a salmon
crouse = Salmon()
##harry is a Hilibut
harry = Halibut()
		