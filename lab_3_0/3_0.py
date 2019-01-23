"""
CSCI 1200
Lab Exercise 3.0

INTRODUCING LISTS

Your task in this lab exercise is to learn to declare lists and to 
perform basic operations on lists. Do all work in Geany IDE 
and follow instructions provided in this code file.

Learning Outcomes
=================
In this lab you will learn:
- How to declare lists
- Add items to list
- Remove items from list
- Sort lists

Evaluation
==========
20 pts. - submitted filename 3_0.py
20 pts. - 3_0.py executes without error
30 pts. - Task 1 meets requirements
30 pts. - Task 2 meets requirements

Execute your code to get instant feedback

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""
#=======================================================================
# TASK 1
#-----------------------------------------------------------------------

# Declare list variable colors that contains following following values:
# red, blue, green, orange, yellow

colors = ['red', 'blue', 'green', 'yellow',]   
print(colors)

# Get length of colors and assign it to number_of_colors.
# Make sure to use the correct python function that returns list length.
# Do not assign literal value.

number_of_colors = -1
print(colors[0]) 

print(colors[-1])


# Get first item in colors list and assign it to first_color.
# Make sure to use correct syntax for accessing items in list.
# Do not assign literal value.

first_color = None

colors =['red', 'blue', 'green', 'yellow']
print(colors[0])


# Get last item in colors list and assign it to last_color
# Make sure to use correct syntax for accessing items in list.
# Do not assign literal value.

last_color = None
print(colors[3])

#=======================================================================
# TASK 2
#-----------------------------------------------------------------------

"""
Pretend you are in a classroom and want to keep track of students
currently in the classroom. We will use a list to keep track of
entering and exiting students. The classroom is initially empty.
"""

# Declare list variable called students. The classroom is currently 
# empty so students should be an empty list.
students=[] 


# Alice enters the classroom. Add 'Alice' to list of students.
students.append('Alice')
print(students)


# Bob enters the classroom. Add 'Bob' to list of students.

students.append('Bob')
print(students)


# Dave enters the classroom. Add 'Dave' to list of students.
students.append('Dave')
print(students)


# Now Bob is done with his work and leaves the room. 
# Remove Bob from the list of students.
students.remove('Bob')
print(students)


# Carol enters the classroom. Add 'Carrrl' to list of students.
students.append('Carrrl')
print(students)


# Oh snap, you misspelled Carol's name. Change 'Carrrl' to 'Carol' 
students[-1]='Carol'
print(students)


# Hall monitor has entered the room and wants to know the names
# of the people in the classroom, in alphabetical order. 
# First sort your list of students from A to Z. 
students.sort()
print(students)
# Then assign the sorted list to variable answer.

answer = students

#=======================================================================
# That's it for today!
# End of Lab Exercise 3.0
#=======================================================================

"""
DO NOT MODIFY BELOW THIS LINE
"""

def output(msg):
	print(msg)
	exit(0)

print(('\n'*4)+('='*50)+('\n INSTRUCTOR FEEDBACK'+'\n')+('='*50)+'\n')

print('Checking Task 1....')
if(len(colors) != 5):
	output('(!) colors list should contain five colors')

if(number_of_colors != 5):
	output('(!) number of colors should equal length of colors')

print('CORRECT: colors list has right length')

if colors[0] != 'red' or first_color != 'red':
	output('(!) first color should be red')

print('CORRECT: colors list contains red')

if colors[-1] != 'yellow' or last_color != 'yellow':
	output('(!) last color should be yellow')

print('CORRECT: colors list contains yellow')
print('\nTask 1 appears to be correct\n\n')

print('Checking Task 2....')
try: students
except NameError: students = None

if(students is None or type(students) is not list):
	output('(!) you must declare list variable called students')

print('CORRECT: students list declared correctly')

if 'Alice' not in students:
	output('(!) students list should contain Alice')

print('CORRECT: Alice is in the classroom')

if 'Dave' not in students:
	output('(!) there should be more students in the classroom')

print('CORRECT: Dave is in the classroom')

if 'Bob' in students and 'Carol' in students:
	output('(!) Bob should not be in students because he already left')

elif 'Bob' not in students and 'Carol' in students:
	print('CORRECT: Bob has left and Carol is present')

if answer is not None and len(answer) > 0 and len(answer) != 3:
	output('(!) there should be 3 students in the classroom')

if answer is not None and len(answer) > 0 and answer != ['Alice' , 'Carol', 'Dave']:
	output('(!) make sure to sort student names')

if answer is not None and (len(answer) == 3):
	print('\nTask 2 appears to be correct')
	print('Good Job!')
else:
	output('(!) Task 2 needs more work')
