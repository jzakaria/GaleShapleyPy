def assign_preferences(person, otherlist):
	rn = range(1,len(otherlist)+1)
	random.shuffle(rn)
	dt = {}
	for choice in rn:
		dt[choice] = False
	person.preferences = dt