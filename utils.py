import random
import person.py

def add_person_to_list(person, list_of_persons):
	person.id = len(list_of_persons.ls)+1
	person.group = list_of_persons.name
	list_of_persons.ls.append(person)

def assign_preferences(person, otherlist):
	rn = range(1,len(otherlist)+1)
	random.shuffle(rn)
	dt = {}
	for choice in rn:
		dt[otherlist[choice]] = False
	person.preferences = dt

def make_random_lists(size):
	men, women = [], []
	for i in range(0,size):
		men[i], women[i] = Person()
	for i in range(0,size):
		assign_preferences(men[i], women)
		assign_preferences(women[i], men)
	return men, women
