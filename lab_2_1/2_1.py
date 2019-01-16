"""
CSCI 1200
Lab Exercise 2.1

VARIABLES AND SIMPLE DATA TYPES

Your task in this lab exercise is to declare and initialize variables 
and manipulate strings, integers and floats. Do all work in Geany IDE 
and follow instructions provided in this code file.

Learning Outcomes
=================
In this lab you will learn:
- How to declare variables
- Concatenate strings
- Change letter case
- Declare integers
- Declare floats
- Perform basic math operations
- Identify and read python comments

Evaluation
==========
20 pts. - submitted filename 2_1.py
20 pts. - 2_1.py executes without error
30 pts. - Task 1 meets requirements
30 pts. - Task 2 meets requirements

Submission
==========
As before, submit your work on D2L or using git.

Earn 5 pts. extra credit by submitting using git by due date.


"""
#***********************************************************************
# TASK 1

# Declare a variable
# Set the string's value to your first name
# Be sure to follow variable naming conventions
# Enter your code in the line below
my_firstname = 'Jon'
print(my_firstname)

# Declare another variable
# Set the string's value to your last name
# Be sure to follow variable naming conventions
# Enter your code in the line below
my_lastname = 'Ingram'
print(my_lastname)

# Print your first and last name to the screen using concatenation
# Include one space between your first and last names


print(my_firstname + " " + my_lastname)

# Declare another variable to hold your full name
# Concatenate the values of your first and last name variables
# Save them as your full name in the line below below

full_name = my_firstname + " " + my_lastname
print(full_name)

# Just to be safe, convert your full name to all lower case below
# Save the value to be the new value of your full name variable


print(full_name.lower())

# Print out your full name again
print(full_name)

# Print out your full name using the title() function
print(full_name.title() + "!")

# Print your full name again, without title()
# This demonstrates you haven't changed the value

print(full_name)
#***********************************************************************
 # for whitespace - do not edit
#***********************************************************************
# TASK 2

# Declare an integer variable
# Give this variable the value of your favorite integer (not zero)
my_variable=5

# Print your variable's value to the screen
print(my_variable)

# Declare another variable with a float value
# Give this variable the value of your favorite float (not zero)
my_float=2.5

# Print this variable's value to the screen
print(my_float)

# Divide your integer by your float (int / float)
# Print this calculation to the screen
print(my_variable / my_float)

# Now divide your float by your integer (float / int)
# Print this calculation to the screen as well
print(my_float / my_variable)

#***********************************************************************
# That's it for today!
# End of Lab Exercise 2.1
