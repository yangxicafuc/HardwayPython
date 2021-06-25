class Parent(object):

	def impilcit(self):
		print("PARENT impilcit()")
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.impilcit()
son.impilcit()