class Parent(object):

	def impilcit(self):
		print("PARENT impilcit()")
		
	def override(self):
		print("PARENT override()")
		
	def altered(self):
		print("PARENT altered()")
		
class Child(Parent):

	def override(self):
		print("CHILD override()")
		
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		print("CHILD altered()")
		print("CHILD, AFTER PARENT altered()")
	
dad = Parent()
son = Child()

dad.impilcit()
son.impilcit()

dad.override()
son.override()

dad.altered()
son.altered()