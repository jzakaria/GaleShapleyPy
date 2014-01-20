class Person:
	def __init__(self):
	    self.id = None
	    self.preference = {}
	    self.engaged = None
	    self.group = None

class PersonList:
	def __init__(self, name=None, ls=[]):
		self.name = name
		self.ls = ls