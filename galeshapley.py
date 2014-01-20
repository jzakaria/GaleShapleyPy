import random

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

def add_person_to_list(person, list_of_persons):
	person.id = len(list_of_persons.ls)+1
	person.group = list_of_persons.name
	list_of_persons.ls.append(person)

def assign_preferences(person, otherlist):
	rn = range(1,len(otherlist)+1)
	random.shuffle(rn)
	dt = {}
	for choice in rn:
		dt[choice] = False
	person.preferences = dt

def high_ranking_partner_not_proposed(person):
	for key in person.preference:
		if not person.preference[key]:
			return key
	return None

#checks if person is free and hasn't proposed to every other partner
def checkPerson(person):
	if person.engaged
		return False
	for partner in person.preferences:
		if not person.preferences[partner]:
			return true
	return false

# I really love list comprehensions
def free_men_who_havent_proposed_to_all_women(men):
	return [m for m in men if checkPerson(m)]

# person 1 proposes to person 2
def propose(person1, person2):
	person1.preferences[person2] = True	

# This is problematic because their ids may be the same therefore
# we somehow need to keep track what list each belongs to
def become_engaged(person1, person2):
	person1.engaged = person2.id
	person2.engaged = person1.id


def galeshapley (men, women):
	set_of_engaged_pairs = []
	ls = free_men_who_havent_proposed_to_all_women(men)
	while ls:
		m = ls[0]
		w = high_ranking_partner_not_proposed(m)
		if not w.engaged
			propose(m, w)
			become_engaged(m, w)
		else
			propose(m,w)
			m1 = w.engaged
			if w_prefers(m, m1):
				become_engaged(m,w)
				m1.engaged = None
				ls.append(m1)
				ls = ls[1:]