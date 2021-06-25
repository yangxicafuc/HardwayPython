## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object (yes, sort of confusing) look at the extra credit
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name, hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary 
		self.salary = salary
		
## Fish is-a object (yes, sort of confusing) look at the extra credit
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass 
	
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a Pet satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a Pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## course is-a Salmon
course = Salmon()

## harry is-a Halibut
harry = Halibut()
		
# dog = Dog("NY")
# print(f"Dog's name is {dog.nickname}")

# dog2 = Dog("Wang")
# print(f"Dog2's name is {dog2.nickname}")

# dog3 = Dog(dog.nickname)
# print(f"Dog3's name is {dog3.nickname}")


#dog.name = "LU"
#print(f"Dog's name is {dog.name}")
#dog.change("WANG")
#print(f"Dog's name is {dog.name}")



##cat = Cat("WANG")
##print(f"Cat's name is {cat.name}")
# person = Person("YANG")
# print(f"Person's name is {person.name}")

# cat = dog
# print(f"Cat's name is {cat.name}")
# cat = person
# print(f"Cat's name is {cat.name}")