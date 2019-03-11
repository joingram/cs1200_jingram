"""
CSCI 1200
Lab Exercise 8.0

FUNCTIONS

In this lab we will learn how to create functions. Focus on writing 
good functions and calling them correctly. Do all work in Geany IDE and 
follow instructions provided in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- declare functions
- specify required parameters
- return values
- call functions

Evaluation
==========
20 pts. - submitted filename 8_0.py
20 pts. - 8_0.py executes without error
30 pts. - Part 1 meets requirements
30 pts. - Part 2 meets requirements

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""


#=======================================================================
# PART 1
#-----------------------------------------------------------------------
# In this part you will create math functions that return values.
#
# Implement functions to perform addition, subtraction, multiplication, 
# division and the remainder (modulo) operation on the two numbers. 
# Write each function to accept the two integers as parameters and 
# to return an integer. Don't forget the docstrings!
#-----------------------------------------------------------------------

def add_numbers(m, n):
	"""Returns the sum of two numbers."""
	return m+n
add_numbers(3,0)

x=add_numbers(3,0)
print(x)
def subtract_numbers(m, n):
	"""Returns the difference of two numbers."""
	return m-n
subtract_numbers(3,2)
z=subtract_numbers(3,2)
print(z)
def multiply_numbers(m, n):
	"""Returns the product of two numbers."""
	return m*n
multiply_numbers(3,2)
m=multiply_numbers(3,2)
print(m)
def divide_numbers(m, n):
	"""Returns the quotient of two numbers."""
	return m/n
divide_numbers(10,2)
d=divide_numbers(10,2)
print(d)
def remainderof_numbers(m, n):
	"""Returns the aquotient of two numbers."""
	return m%n
remainderof_numbers(11,2)
r=remainderof_numbers(11,2)
print(r)



#=======================================================================
# PART 2
#-----------------------------------------------------------------------
# In this part you will write an input program where you perform 
# the following steps:
# 
# 1. Welcome the user to Lab Exercise 8.0
#
# 2. Prompt for the user's name. Receive the name into the program and 
# save it as the value of a name variable.
#
# 3. Prompt the user two integers. Receive the numbers and save them as 
# variable values. 
#
# 4. Make function calls to perform the calculations you created in 
# part 1. Ensure you send both numbers as arguments to the functions. 
# Write the results of  the function calls out to the screen. 
#
# See sample output here: https://i.imgur.com/l3xEoJP.png
#-----------------------------------------------------------------------

name=input("enter your name")
print("Thanks" + name + "!")
first_interger=int(input("Give me your first interger" + ""))
second_interger=int(input("Give me your second interger"))
print( "Great," + name + " your numbers are" + str(first_interger) + "and" + str(second_interger)) 

print("I'll now add" )
print(str(subtract_numbers(first_interger,second_interger)) + " is your answer")

print("Thanks" + name + "!")

print( "Great," + name + " your numbers are" + str(first_interger) + "and" + str(second_interger)) 
print("I'll now subtract")  
print(str(subtract_numbers(first_interger,second_interger)) + " is your answer")


print( "Great," + name + " your numbers are" + str(first_interger) + "and" + str(second_interger)) 
print("I'll now multiply")
print(str(multiply_numbers(first_interger,second_interger)) + "is your answer")



print( "Great," + name + " your numbers are" + str(first_interger) + "and" + str(second_interger)) 
print("I'll now divide") 
print(str(divide_numbers(first_interger,second_interger)) + "is your answer") 

print( "Great," + name + " your numbers are" + str(first_interger) + "and" + str(second_interger)) 
print("I'll now divide the numbers") 
print(str(remainderof_numbers(first_interger,second_interger)) + " is your answer")

#=======================================================================
# That's it for today!
# End of Lab Exercise 8.0
#=======================================================================
