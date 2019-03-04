"""
CSCI 1200
Lab Exercise 7.1

USER INPUT AND WHILE LOOPS (CONT.)

In this lab we will practice some fundamental concepts related to while 
loops. Do all work in Geany IDE and follow instructions provided 
in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- use nested while loops
- use inplace operators (perhaps)
- handle user input

Evaluation
==========
20 pts. - submitted file game.py
20 pts. - game.py executes without error
60 pts. - game.py meets requirements

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""

'''DO NOT EDIT'''
import random
import os
new_answer = lambda a,b : random.randint(a,b)
clear = lambda: os.system('cls')
'''END'''
	
#=======================================================================
# HIGHER OR LOWER GAME
#-----------------------------------------------------------------------
# In this exercise we will create a game called higher or lower.
#
# The idea of this game is simple:
# The computer will choose a random number within known limits.
# The player's task is to guess that number. The player will continue
# to guess the value until they guess correctly.
#
# To create this game you will need to use while loop, get input
# from user, and write conditional statements to check if player has 
# guessed the correct value, and more! However, you should already be 
# familiar with all these building blocks you need to create this game.
#
# After you are done, if you want, you can add some custom flair
# to your game using for example this ASCII art generator:
# http://patorjk.com/software/taag/
#-----------------------------------------------------------------------

# You may change these number to make your game easier/harder
min_number = 0 	 
max_number = 100 


# Greet the player. Ask them if they want to:
# [1] Start Game
# [2] Quit
# Handle player's response accordingly.


# If player starts a new game, create variable called answer like so:
# answer = new_answer(min_number, max_number)


# Create a variable counter to keep track of how many times
# player has tried to guessed the answer. This should initially be 0.


# Print to console these instructions:
# "I'm thinking of a number between A and B", where A is min_number
# and B is max_number


# Ask player to guess what they think the answer is. 
# Increment counter by 1.


# Compare player's guess to the answer you have.
# If player's guess is below answer, print "higher"
# If player's guess is above answer, print "lower"
# Then go back to the code section where you ask player to guess



# If player's guess matches answer, say it is correct, print the number 
# of times the player guessed before getting the correct answer and end 
# game. Here you should return to the initial menu with options to 
# choose start game/quit. If you want to clear the previous input you 
# can use clear()




#=======================================================================
# That's it for today!
# End of Lab Exercise 7.1
#=======================================================================
