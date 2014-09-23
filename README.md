The infection specifications were implemented using Python, SQLAlchemy and SQlite.

The infection.py module contains all the infection methods.
The tests.py module contains all the tests

To use:
1. install SQLAlchemy: in the command line type "pip install SQLAlchemy==0.9.7"
2. in the main directory, open a python intepreter: in the command line type "python"
3. type: from infection import *
4. add users with the command: a = add_user("A") where a, and "A" can be any variable.
	Note that only one student can have each unique name
5. add coaching relationships: add_coaching(a, b) where a is the coach and b is the student,
	and both are variables created by add_user method.
6. test total_infection and limited_infection, inputing the object of the student, 
	not the name (i.e a not "A")
7. to see who was infected: infection_report()
8. to uninfect all students: reset_infection()

**To run the tests, type the following in the python interpreter: 
	1. from tests import *
	2. run_tests()

**If you import the test module, you can do additional tests on the set of users specified in it.

**Additional modifications
infect_n() : First, look for a connected component of size n. If it finds it, it infects it. 
			 Otherwise, it does nothing.
