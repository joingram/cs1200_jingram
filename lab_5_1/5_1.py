"""
CSCI 1200
Lab Exercise 5.1

IF STATEMENTS (CONT.)

In this lab we will learn how to use if statements in more complex
situations. Do all work in Geany IDE and follow instructions provided 
in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- use if statements with loops and lists
- write more complex conditional statements with and and or


Evaluation
==========
20 pts. - submitted filename 5_1.py
20 pts. - 5_1.py executes without error
20 pts. - Part 1 meets requirements
40 pts. - Part 2 meets requirements


Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""


#=======================================================================
# PART 1
#-----------------------------------------------------------------------
# 
# In this exercise we will practice using if statements with loops  
#
#-----------------------------------------------------------------------

''' DO NOT EDIT '''
todays_movies = [
    'The Lego Movie 2: The Second Part', 'Alita: Battle Angel', 
    "Isn't it Romantic", 'Happy Death Day 2U', 'What Men Want', 
    'Cold Pursuit', 'The Prodigy', 'The Upside', 'Casablanca'
]
want_to_see = [
    'Cold Pursuit', 'Captain Marvel', 'Alita: Battle Angel', 'Joker'
]
''' END '''


# Pretend you are going to go see a movie. 
#
# The theater show different movies each day, however, you are only 
# interested in seeing certain movies.
#   
# Write a for loop where you go through each movie that is currently
# playing. 
#
# If the movie is one of the ones you want to see, 
# print 'I want to see ' and the name of the movie (use concatenation)
#
# If you are not interested in the movie, 
# print 'Do not want to see ' and the name of the movie (concatenate)
#
# Hint: the list of movies shown in the theater is stored in variable
# todays_movies, variable with movies you want to see is want_to_see










# Some of the movies you want to see are future releases, so you
# cannot see them yet.  
#
# Write a for loop where you go through each movie you want to see.
#
# If that movie is already showing in a theater
# print 'I can go see ' and the name of the movie (concatenate)
#
# If the movie is a future release
# print the movie name and ' will be in theaters soon' (concatenate)







''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#=======================================================================
# PART 2
#-----------------------------------------------------------------------
#
# Imagine a scenario where we are creating a simple registration page
# for our app. This is a page where user chooses their username etc. 
# then presses submit. 
#
# Typically when working with user input like this, we have to be 
# defensive in checking the values user provides. Often times users
# may provide values that are invalid and we need to tell them to fix
# the input. This process in general is called input validation. 
# 
# In this part we will write some basic input validation checks using
# the python syntax we have learned so far. 
#
#-----------------------------------------------------------------------

''' DO NOT EDIT '''
existing_users = ['superuser', 'admin', 'anna', 'johnny', 'user1']
input_is_valid = True
''' END '''

# Declare a string variable called username. Set the value to any value 
# you want.




# Declare a string variable called email_address. Set the value to any
# value you want




# Declare an integer variable called user_age. Set the value to any
# value you want.




'''
Great. Now let us assume the variables above are the values provided
by user when they completed our registration form. We need to make 
sure these inputs are valid, then take appropriate action.
'''

# First let's validate username. We want to check that username meets
# following requirements:
#
#    * length is at least 4 characters, and 
#    * username is not assigned to any existing user 
#
# Write the appropriate statement where you test these conditions. 
# If username DOES NOT meet this criteria, set input_is_valid = False
#
# Hint: existing_users is a list of all existing usernames 










'''---------------------------------------------------------------------
Another Hint: if you write an if-else statement but want to leave
the if body empty, you can use special keyword pass to do this, example:
   
if something:                            if something:
else:                                        pass
    something_else                       else:
                                             something_else
                                                
DOES NOT WORK ↑↑↑                        WORKS ↑↑↑
---------------------------------------------------------------------'''



# Next lets validate email_address. We will accept the value if it 
# meets these requirements:
#
#   * email contains ".com" or ".edu"
#
# Write the appropriate statement where you test these conditions. If 
# email_address DOES NOT meet this criteria, set input_is_valid = False
#
# Hint: the syntax for checking if string contains some value is 
# the same as checking if list contains some value. 








# Lastly lets validate user_age. User must be:
#
#   * at least 13 years old
#   * not older than 19, this app is for teens
#
# Write the appropriate statement where you test these conditions. If 
# user_age DOES NOT meet this criteria, set input_is_valid = False









# Now we have completed all validation checks. 
# Let's tell the user if their input is acceptable of not. 
#
# Write an if statement where:  
# if user input is valid, print 'Welcome ' username (use concatenation) 
# if user input is not valid, print 'Check inputs and try again'
#
# Hint: input_is_valid tells us if user passed all checks or not








'''
TIP: TO check your work change username, email_address and/or user_age 
values and execute your code again. Typically you want to test your code 
for different cases where inputs are valid/invalid to make sure the 
code performs correctly with every possible input.
'''
#=======================================================================
# That's it for today!
# End of Lab Exercise 5.1
#=======================================================================
