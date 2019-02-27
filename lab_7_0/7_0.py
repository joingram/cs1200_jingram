"""
CSCI 1200
Lab Exercise 7.0

USER INPUT AND WHILE LOOPS

In this lab we will learn how to use while loops and receive input 
from a user. Do all work in Geany IDE and follow instructions provided 
in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- ask user for input
- write input prompts
- write while loops
- terminate a while loop based on a condition
- convert data from string to int
- recap how to use conditional statements 

Evaluation
==========
20 pts. - submitted filename 7_0.py
20 pts. - 7_0.py executes without error
60 pts. - Assignment meets requirements

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""


#=======================================================================
# YOUR ASSIGNMENT
#-----------------------------------------------------------------------
# Imagine you are writing software for Cafe 1200, a casual dining spot 
# with wait times. 
#
# As groups of people come in, you want to get their last name and 
# number of people in their party. Then, based on their answer, you 
# will provide an estimated wait time until their table is ready.
#
# The average wait times at Cafe 1200 are as follows:
# - A party size of 1 - 2 can be seated immediately
# - A party size of 3 - 4 can be seated in approximately 10-12 minutes
# - A party size of 5 - 8 can be seated in approximately 20-25 minutes
# - A party size of 9 - 12 can be seated in approximately 30-40 minutes
# - A party size of greater than 12 will wait at least an hour
# - A party size of zero or less isn't funny; however your program
#   should be able to handle this edge case 
#
# Other instructions:
# - interact in a friendly manner with the customers
# - be exact and concise when writing prompts
# - After providing estimated wait time, you should ask user 
#   if they want to continue to next group of people or quit.
#-----------------------------------------------------------------------


# Hint 1: start by greeting the people

# Hint 2: ask for name and then ask for size of party

# Hint 3: based on their answer, determine the wait time

# Hint 4: output the wait time

# Hint 5: ask user if they want to continue or quit. 

while True:
	
	print("Hello!" + " " + "What is your name and party size")

	Name = input("What is the name? ")
	party_size = input("What is party size? ")
	party_size = int(party_size)

	if party_size <= 0:

		print("Give me real number please")
	elif party_size <= 3:
		print("We can seat you now") 
	elif party_size <= 4:
		print("We can seat you in about 10-12 minutes")
	elif party_size <= 5:
		print("We can seat you in about 20-25 minutes")
	elif party_size <= 6:
		print("We can seat you in about 20-25 minutes")
	elif party_size <= 7:
		print("We can seat you in about 20-25 minutes")
	elif party_size <= 8:
		print("We can seat you in about 20-25 minutes")
	elif party_size <= 9:
		print("We can seat you in about 30-40 minutes")
	elif party_size <= 10:
		print("We can seat you in about 30-40 minutes")
	elif party_size <= 11:
		print("We can seat you in about 30-40 minutes")
	elif party_size <= 12:
		print("We can seat you in about 40-60 minutes")
	elif party_size >= 12:
		print("We can seat you in about an hour")

	yes_no= input("Would you like to continue? Y or n")

	if yes_no.lower() == "n":
		break
	

# ~ while True:
	# ~ party_size = input(prompt)
	
	# ~ if party_size == False:
		# ~ prin
		
	# ~ else:
	# ~ print("Alright," + name.title(), + int(party_size))


	


# ~ prompt = "\Enjoy your dinner"
# ~ prompt += "\nEnter 'quit' to end the program. "
# ~ message = ""
# ~ while message != 'quit':
   # ~ message =input(prompt)
# ~ print(message)
# ~ print()

#=======================================================================
# That's it for today!
# End of Lab Exercise 7.0
#=======================================================================
