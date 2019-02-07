"""
CSCI 1200
Lab Exercise 4.1

WORKING WITH LISTS, PT 2

In this lab we will we will learn about slicing lists and tuples.
Do all work in Geany IDE and follow instructions provided in this 
code file.

Learning Outcomes
=================
In this lab you will learn how to:
- slice lists
- declare and use tuples

Evaluation
==========
20 pts. - submitted filename 4_1.py
20 pts. - 4_1.py executes without error
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

# In this part we will learn how to slice lists. 
# To help visualize this concept we will use a hamburger. See this 
# image to get a better idea (copy paste this link to your browser):  
#
# https://i.imgur.com/PDQsn3L.png


# we can convert the image to a python list like so:

hamburger = [
    'bottom bun', 'patty', 'cheese', 'bacon', 'lettuce', 'onions', 
    'tomato', 'pickles', 'ketchup', 'mustard', 'top bun'
]


# Next we will create variations of the burger by slicing it.

# 1. Using python list slice syntax, create a hamburger without bun,
# i.e. you must create a slice that excludes bottom and top bun

bunless = None


# 2. Using python list syntax, create a hamburger with:
# 'tomato', 'pickles', 'ketchup', 'mustard', 'top bun'

veggie = None


# 3. Using python list syntax, create a hamburger with:
# 'patty', 'cheese', 'bacon'

keto_friendly = None


# 4. Using python list slice syntax, create a hamburger with:
# 'bottom bun', 'cheese', 'lettuce', 'tomato', 'ketchup' and 'top bun'

alternate = None


# 5. Using python list slice syntax, create a hamburger with: 
# 'bottom bun', 'patty', 'cheese', 'ketchup', 'mustard', 'top bun'.
# Here you may need to concatenate two slices. Remember you can
# concatenate lists using + symbol, example: list_1 + list_2

basic = None


#=======================================================================
# PART 2
#-----------------------------------------------------------------------


# In this part we will work with tuples.

# Create a tuple called my_tuple and assign following values to it: 
# 1, 'python', 5.6, True 




# Notice these are different data types. While it does not happen
# often, in python lists and tuples can contain values of different data
# types. Print my_tuple to verify that mixing types is in fact possible.




# While you cannot change values in a tuple, you can access its values 
# just like you would access values in a list. To test this, write a
# for loop and print out each value in my_tuple 




# We can also access tuple values using their index, just like we would 
# access items in a list. To test this, assing the second value in the 
# tuple to variable programming_language.




# In order to change the values in a tuple we must reassign a new value 
# to the variable that holds the tuple, in this case my_tuple. 
# Change my_tuple to contain new values: 8, 'Python', 3.7, False 




# print my_tuple to verify the values have changed




#=======================================================================
# That's it for today!
# End of Lab Exercise 4.1
#=======================================================================


"""
DO NOT MODIFY BELOW THIS LINE
"""

def output(msg):
    print(msg)
    exit(0)

print(('\n'*4)+('='*50)+('\n INSTRUCTOR FEEDBACK'+'\n')+('='*50)+'\n')

print('Checking Part 1....')

try: bunless
except NameError: bunless = None

if(bunless is None or type(bunless) is not list):
    output('(!) create bunless hamburger')

if(bunless != ['patty', 'cheese', 'bacon', 'lettuce', 'onions', 
    'tomato', 'pickles', 'ketchup', 'mustard']):
    output('(!) Bunless burger should include all ingredients except buns') 
else: 
	print('Bunless burger is correct')     
    

try: veggie
except NameError: veggie = None

if(veggie is None or type(veggie) is not list):
    output('(!) create a veggie burger')

if(veggie != ['tomato', 'pickles', 'ketchup', 'mustard', 'top bun']):
    output('(!) Veggie burger ingredients are not correct')      
else:
	print('Veggie burger is correct')     
    

try: keto_friendly
except NameError: keto_friendly = None

if(keto_friendly is None or type(keto_friendly) is not list):
    output('(!) create a keto_friendly burger')

if(keto_friendly != ['patty', 'cheese', 'bacon']):
    output('(!) Keto friendly burger ingredients are not correct')      
else:
	print('Keto burger is correct')     
    

try: alternate
except NameError: alternate = None

if(alternate is None or type(alternate) is not list):
    output('(!) create an alternate burger')

if(alternate != [ 'bottom bun', 'cheese', 'lettuce', 'tomato', 
	'ketchup', 'top bun']):
    output('(!) Alternate burger ingredients are not correct')      
else:
	print('Alternate burger is correct')     
    

try: basic
except NameError: basic = None

if(basic is None or type(basic) is not list):
    output('(!) create a basic burger')

if(basic != [ 'bottom bun', 'patty', 'cheese', 'ketchup', 'mustard', 
	'top bun']):
    output('(!) Basic burger ingredients are not correct')      
else:
	print('Basic burger is correct')     
    
print('Great! You have finished the burger challenge.')



print('\nChecking Part 2....')

try: my_tuple
except NameError: my_tuple = None

if(my_tuple is None or type(my_tuple) is not tuple):
    output('(!) create tuple called my_tuple')

try: programming_language
except NameError: programming_language = None

    
if(programming_language is None and my_tuple != (1, 'python', 5.6, True)):
    output('(!) my_tuple values are not correct')      

print('my_tuple is declared correctly')    
    

if(programming_language is None or type(programming_language) \
    is not str or programming_language != 'python'):
    output('(!) create variable programming_language and assign\n' + \
    '    the second value in my_tuple to it')
print('programming_language is assigned correctly')
    
if(my_tuple != (8, 'Python', 3.7, False)):
    output('(!) my_tuple values must change')      
print('tuple value changed correctly')

print('Good Job! Part 2 appears to be correct.')  

