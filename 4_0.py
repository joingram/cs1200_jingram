"""
CSCI 1200
Lab Exercise 4.0

WORKING WITH LISTS

In this lab we will we will learn about for loops and indentation.
Do all work in Geany IDE and follow instructions provided in this 
code file.

Learning Outcomes
=================
In this lab you will learn how to:
- declare and use for loops
- indent code and fix indentation errors
- use range function 
- find min, max, and sum of numeric list


Evaluation
==========
20 pts. - submitted filename 4_0.py
20 pts. - 4_0.py executes without error
20 pts. - Part 1 meets requirements
20 pts. - Part 2 meets requirements
20 pts. - Part 3 meets requirements


Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""

#=======================================================================
# PART 1
#-----------------------------------------------------------------------
#
# In this part your will practice writing for loops to perform 
# operations on list items. We will do this a few times to make sure 
# you have a good understanding of how to write for loops.
#
#-----------------------------------------------------------------------


# 1.a) using the list of cities, write a for loop where you print
# the name of each city 

cities = [ 
    'Athens', 'Atlanta', 'Augusta', 'Brunswick', 'Carrollton',
    'Columbus', 'Gainesville', 'Kennesaw', 'Macon', 'Marietta', 
    'Savannah', 'Statesboro', 'Stockbridge', 'Valdosta', 'Waycross'
]

for cities in cities:
	print(cities)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 1.b) using the list of sandwiches, write a for loop where you
# first print the name of the sandwich, then append the sandwich to 
# my_sandwiches. After running the loop, both lists should contain 
# the same values. Print both lists to check your work.

sandwiches = [
	'Italian Beef', 'Cheesesteak', 'French Dip', 'BLT', 'Lobster Roll',
	"Po' Boy", 'Ham and Cheese', 'Patty Melt', 'Reuben', 'Sloppy Joe',
	'Roast beef', 'Hot dog', 'Cuban sandwich', 'Pulled Pork'
]
for sandwiches in sandwiches:
    print(sandwiches)
my_sandwiches = [sandwiches]
for my_sandwiches in my_sandwiches:
	print(my_sandwiches)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 1.c) Using the list of numbers, write a for loop where you:
# raise each number to second power, minus 1, then add it to result.
# After running the loop, result should equal 2450. 
# Print result to check your work.

numbers = list(range(20))
result = 0
print(numbers)

for number in numbers:
	result = result + (number ** 2 -1)

print(result)



#=======================================================================
# PART 2
#-----------------------------------------------------------------------
#
# By now you should have a pretty good idea how to use for loops and
# indent code sections. Given what you know, you should also be able
# identify when code sections contain errors and be able to fix them.
# 
# Therefore, in Part 2, your task is to review following code blocks 
# that contain errors, and fix them. Once the two sections execute 
# without error you are done with Part 2.
#
# Remove the triple quotes ''' around each code block to run the code
# 
#-----------------------------------------------------------------------


 

for i in range(10):
    print(i)








cars = ['Audi', 'BMW', 'Ford', 'Genesis', 'GMC', 'Honda', 'Toyota']
for car in cars:
    print('I like ' + car + '!')
    
print('There were ' + str(len(cars)) + ' in total')
print('Honda is my favorite')




#=======================================================================
# PART 3
#-----------------------------------------------------------------------


# Create a numerical (integer) list with 1,000,000 items, with values 
# from 0 to 999,999. Hint: Use the range() function.
numbers = list(range(0,1000000))


# Write the length of the list out to the screen. Ensure you have 
# 1,000,000 items in your list. Hint: Use the len() function.
many_numbers = len(numbers)
print(many_numbers)

# Print the smallest item value in the list out to the screen.
minimum = min(numbers)
print(minimum)


# Print the largest item value in the list out to the screen. 
maximum = max(numbers)
print(maximum)


# Print the sum of all the item values out to the screen.  
sum_all = sum(numbers)
print(sum_all)



#=======================================================================
# That's it for today!
# End of Lab Exercise 4.0
#=======================================================================
