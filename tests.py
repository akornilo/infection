from infection import *

# create set of users
a = add_user("A")
b = add_user("B")
c = add_user("C")
d = add_user("D")
e = add_user("E")
f = add_user("F")
g = add_user("G")
h = add_user("H")

all_students = [a,b,c,d,e,f,g,h]

add_coaching(a, b)
add_coaching(b, c)

add_coaching(d, e)
add_coaching(e, f)
add_coaching(f, d)
add_coaching(h, e)

''' total infection on middle of chain '''
def test_one():
	total_infection(b)
	sol = [True, True, True, False, False, False, False, False]
	if [is_infected(x) for x in all_students] == sol:
		print "Pass test 1"
	else:
		print "Fail test 1, Test:", my_sol,"Actual:", sol
	reset_infection()

''' total infection with cycle '''
def test_two():
	total_infection(d)
	sol = [False, False, False, True, True, True, False, True] 
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 2"
	else:
		print "Fail test 2, Test:", my_sol,"Actual:", sol
	reset_infection()
''' basic limited test '''
def test_three():
	limited_infection(b, 2)
	sol = [False, True, True, False, False, False, False, False]
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 3"
	else:
		print "Fail test 3, Test:", my_sol,"Actual:", sol
	reset_infection()

''' basic limited test '''
def test_four():
	limited_infection(b, 3)
	sol = [True, True, True, False, False, False, False, False]
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 4"
	else:
		print "Fail test 4, Test:", my_sol,"Actual:", sol
	reset_infection()

''' infect everyone '''
def test_five():
	limited_infection(g, 8)
	sol = [True, True, True, True, True, True, True, True]
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 5"
	else:
		print "Fail test 5, Test:", my_sol,"Actual:", sol
	reset_infection()

''' pick coach with most infected students '''
def test_six():
	limited_infection(e, 3)
	sol = [False, False, False, True, True, True, False, False]
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 6"
	else:
		print "Fail test 6, Test:", my_sol,"Actual:", sol
	reset_infection()

def test_seven():
	infect_n(3)
	sol = [True, True, True, False, False, False, False, False]
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 7"
	else:
		print "Fail test 7, Test:", my_sol,"Actual:", sol
	reset_infection()

def test_eight():
	infect_n(2)
	sol = [False, False, False, False, False, False, False, False]
	my_sol = [is_infected(x) for x in all_students]
	if my_sol == sol:
		print "Pass test 8"
	else:
		print "Fail test 8, Test:", my_sol,"Actual:", sol
	reset_infection()

def run_tests():
	test_one()
	test_two()
	test_three()
	test_four()
	test_five()
	test_six()
	test_seven()
	test_eight()