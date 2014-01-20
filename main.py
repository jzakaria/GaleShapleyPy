import galeshapley.py
import utils.py

def check_arg_int(str):
	for i in str:
		if not str[i].isdigit():
			return False
	return True

if _name_ == "main":
	user_input = raw_input("Please enter the size of the lists")
	while not check_arg_int(user_input):
		user_input = raw_input("Please enter a numerical value")
	user_input = int(user_input)
	men, women = make_random_lists(user_input)
	galeshapley(men, women)