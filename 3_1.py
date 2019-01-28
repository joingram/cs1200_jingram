"""
CSCI 1200
Lab Exercise 3.1

INTRODUCING LISTS, PT. 2

Lists are a powerful feature in python and for any true pythonista
it is important to know how to work with them. In this lab we will 
continue extending our skills on working with lists. Do all 
work in Geany IDE and follow instructions provided in this code file.

Learning Outcomes
=================
In this lab you will learn:
- declaring lists
- updating list values
- adding list values
- sorting lists

Evaluation
==========
20 pts. - submitted filename 3_1.py
20 pts. - 3_1.py executes without error
25 pts. - Part 1 meets requirements
25 pts. - Part 2 meets requirements
10 pts. - Part 3 meets requirements

Execute your code to get instant feedback

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""

#=======================================================================
# BACKGROUND
#-----------------------------------------------------------------------
""" 
 
 In the programming world, there are many well-kept secrets that are
 only known to a select few. Well, today is your lucky day! 

 The python overlords have granted you the opportunity to get 
 in on one of these secrets if, and only if, only you are able to 
 successfully follow their instructions. You must complete a 3-part
 challenge and at the end a secret will be revealed.
 
 Here are some words of wisdom to help you on your journey:
 
 "Be very careful as you progress through this mission. Accuracy is very 
 important. Pay attention to indexes. Good Luck my friend!"
 
"""

#=======================================================================
# PART 1
#-----------------------------------------------------------------------

# In this part, first declare list named part_1. This list will 
# initially hold following string values: r, i, t, n, o, y  
part_1 = ['r', 'i', 't', 'n', 'o', 'y']


# sort part_1 in reverse alphabetical order Z-A
part_1.sort(reverse=True)


# add string 's' to the end of part_1
part_1.append('s')


# insert string 'p' to the first position of part_1
part_1.insert(0, 'p')


# change part_1 value at index 3 to 'h'   
part_1[3]='h'


#=======================================================================
# PART 2
#-----------------------------------------------------------------------

# Declare another list, this time part_2. This list will initially
# contain following string values: t,e,m,w,o,z
part_2=['t', 'e', 'm', 'w', 'o', 'z']


# Sort part_2 in alphabetical order A-Z
part_2.sort()



# Insert string "e" to position -2 in the list
part_2.insert(-2, 'e')


# Change the currently last index, -1, to "a"
part_2[-1]='a'


# Change the value at index 3 to "s"
part_2[3]='s'


# Reverse the list (not alphabetical sort!), i.e. apply an
# operation that moves first item to last position, 
# second item to second to last, etc.
part_2.reverse()



#=======================================================================
# PART 3
#-----------------------------------------------------------------------

"""
 Fun fact! Python makes it really easy to concatenate lists. 
 You only need the plus operator. Example:
 
 new_list = list_1 + list_2
 
"""

# In this part your task is to concatenate part_1 and part_2, to 
# discover a hidden secret message.

secret = part_1 + part_2

# For sanity checking, you might want to print out the secret and see 
# what it says. Did you get it? 

print(secret)

# You can also try this command: print("".join(secret))

print("".join(secret))

#=======================================================================
# That's it for today!
# End of Lab Exercise 3.1
#=======================================================================


"""
DO NOT MODIFY BELOW THIS LINE
"""

def output(msg):
	print(msg)
	exit(0)

print(('\n'*4)+('='*50)+('\n INSTRUCTOR FEEDBACK'+'\n')+('='*50)+'\n')

print('Checking Part 1....')

try: part_1
except NameError: part_1 = None

if(part_1 is None or type(part_1) is not list):
	output('(!) you must declare list variable called part_1')
	
if part_1 == list('pythonis'):
	print('\nPart 1 is correct')
	print('Good Job!')
else:
	output('(!) Part 1 needs more work')	
	
print('\nChecking Part 2....')
	
try: part_2
except NameError: part_2 = None

if(part_2 is None or type(part_2) is not list):
	output('(!) you must declare list variable called part_2')
	
if part_2 == list('awesome'):
	print('\nPart 2 is correct')
	print('Good Job!')
else:
	output('(!) Part 2 needs more work')	

print('\nChecking Part 3....')

if secret == list('pythonisawesome'):
	print('\nPart 3 is correct')
	print('Good Job!')
else:
	output('(!) Part 3 needs more work')	
