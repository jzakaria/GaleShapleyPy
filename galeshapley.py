import person.py

def high_ranking_partner_not_proposed(person):
	for choice in person.preference:
		if not person.preference[choice]:
			return choice
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
	person1.engaged = (person2.group, person2.id)
	person2.engaged = (person1.group, person1.id)


def galeshapley (men, women):
	set_of_engaged_pairs = []
	ls = free_men_who_havent_proposed_to_all_women(men)
	while ls:
		m = ls[0]
		w = high_ranking_partner_not_proposed(m)
		if w:
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