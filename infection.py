from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import random
import heapq

''' Set-up User database ''' 
# Create in memory sqlite table and associated structures
engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('coaches', Integer, ForeignKey('users.name'), primary_key=True),
    Column('students', Integer, ForeignKey('users.name'), primary_key=True)
)

class User(Base):
	__tablename__ = 'users'

	name = Column(String, primary_key=True)
	infected = Column(Boolean, default=False)
	students = relationship("User", 
							secondary=association_table, 
							backref="coaches",
							primaryjoin=name==association_table.c.coaches,
                       		secondaryjoin=name==association_table.c.students)


Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

''' User Methods '''
# add user with specified name. If given name in records, this will fail.
def add_user(name):
	user = User(name=name)
	session.add(user)
	session.commit()
	return user

# add coach to student relationship
def add_coaching(coach, student):
	coach.students.append(student)
	session.commit()

# return whether current user is infected
def is_infected(user):
	return user.infected

''' Infection Methods '''

# infects user, returns int based on if infection is new
def infect(user):
	if user.infected:
		return 0
	user.infected = True
	session.commit()
	return 1

# infects all of this coach's students and returns num new infected
def infect_students(coach):
	return sum([int(infect(x)) for x in coach.students])

# infect all users associated with the given one
def total_infection(user):

	def visit(user, visited):
		if user.name in visited:
			return visited

		visited.add(user.name)
		infect(user)

		for s in user.students:
			visited = visit(s, visited)

		for c in user.coaches:
			visited = visit(c, visited)

		return visited

	visit(user, set())

# infect about the number of users, including specified user and his students
# implemented as specified in interview
def limited_infection(user, number):
	count = infect(user)
	# infect all the students of this coach
	count += infect_students(user)

	if count >= number:
		return

	# Put all of the user's coaches in a PQ based on infected students
	coachPQ = []

	# heapq implementation uses minheap, so use negatives to prioritize 
	# based on max infected students of coach.
	for c in user.coaches:
		heapq.heappush(coachPQ, (-1 * sum([int(x.infected) for x in c.students]), c))

	while count < number and coachPQ:
		num, coach = heapq.heappop(coachPQ)
		count += infect(coach)
		count += infect_students(coach)

	if count >= number:
		return

	# if still need to infect more, pick random user
	all_users = session.query(User).all()
	randPos = int(random.random() * len(all_users))

	limited_infection(all_users[randPos], number - count)


''' try to infect a total component of size n '''
''' returns True or False based on success '''
def infect_n(n):

	# identify all conencted components
	all_students = session.query(User).all()

	components = {i:all_students[i] for i in range(len(all_students))}
	mapping = {all_students[i].name : i for i in range(len(all_students))}
	

	def touch(start,i,visited):
		if i in visited:
			return visited

		# mark current vertex as visited
		visited.add(i)

		current = components[i]

		# associate it with component
		components[i] = start
		
		for x in current.students:
			index = mapping[x.name]
			visited = touch(start, index, visited)

		for x in current.coaches:
			index = mapping[x.name]
			visited = touch(start, index, visited)

		return visited

	starts = {}

	for i in components:
		# have not touched this vertex yet
		if all_students[i] == components[i]:
			touch(components[i], i, set())
			starts[all_students[i].name] = 0

	for i in components:
		starts[components[i].name] += 1

	for s in starts:
		if starts[s] == n:
			for i in components:
				if components[i].name == s:
					infect(all_students[i])
			return True
	return False


# report infection status of all users
def infection_report():
	for x in session.query(User).all():
		print x.name, x.infected

# uninfect all users
def reset_infection():
	for x in session.query(User).all():
		x.infected = False
	session.commit()


