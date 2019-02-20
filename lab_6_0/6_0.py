"""
CSCI 1200
Lab Exercise 6.0

DICTIONARIES

In this lab we will learn how dictionaries use keys to access 
values. Do all work in Geany IDE and follow instructions provided 
in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- declare dictionaries
- access dictionary values
- loop over dictionary items


Evaluation
==========
20 pts. - submitted filename 6_0.py
20 pts. - 6_0.py executes without error
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
''' DO NOT EDIT '''
import random
num_doors = 6
seed = random.randint(0, num_doors-1)
val = [1 if x == seed else 0 for x in range(0, num_doors)]
doors = dict(zip(list('ABCDEF'), val))
''' END '''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  BACKGROUND
  In part 1 we will practice the idea how dictionaries use *keys* 
  to access *values*. Imagine in front of you are 6 doors:
 
       ___    ___    ___    ___    ___    ___
      |   |  |   |  |   |  |   |  |   |  |   |
      | A |  | B |  | C |  | D |  | E |  | F |
      |   |  |   |  |   |  |   |  |   |  |   |
   -----------------------------------------------
 
  Each door is locked and you must use a key to see what is behind
  the door. Behind 1 of the doors is a surprise. This special door 
  will change places every time you run the program. 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Your task is to write code that reveals the door that contains
# the suprise. Do as follows:

# 1. Write a for loop where you go through each dictionary item.
#    The name of the dictionary is ‘doors’
#
# 2. Access the value behind each door. 
#    If the value is 1 you have found the suprise and you should 
#    print: "Jackpot! Surprise is behind door X" where X is the 
#    door key. If the value is not 1, print: Not behind door X. 
#
# Hint: it may help to run print(doors) a few times to see what the 
# dictionary looks like and how the special door changes place each time

print(doors)  









''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#=======================================================================
# PART 2
#-----------------------------------------------------------------------
#
# In this part we will practice declaring dictionaries and 
# adding values to it. In fact, let's create and work with a dictionary 
# of dictionaries!
#
# Your mission in this lab exercise is to create a dictionary of three 
# cities. Each city will itself be a dictionary. In essence, you're 
# creating a dictionary of dictionaries.
#
# After creating the dictionary of dictionaries, write out the city 
# names and all city info. 
#-----------------------------------------------------------------------



# 1. Create a dictionary named ‘cities’. Select the names of three U.S. 
# cities (your choice) as keys in your dictionary. 








# 2. Create a dictionary of information about each city. 
# Include the: 
#   1) county the city is in 
#   2) state the city is in 
#   3) population of the city
# Use online sources to obtain the county and population information.








# 3. After creating the dictionary, print the name of each city and all 
# the information you have stored about that city. See this example:
# https://i.imgur.com/UhEFrEV.png







#=======================================================================
# That's it for today!
# End of Lab Exercise 6.0
#=======================================================================
