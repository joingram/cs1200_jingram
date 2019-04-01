"""
CSCI 1200
Lab Exercise 10.1

JSON FORMAT

In this lab you will learn how to use JSON data format. Do all work 
in Geany IDE and follow instructions provided in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- parse JSON data
- save JSON data
- Review file read and write methods

Evaluation
==========
20 pts. - submitted filename 10_1.py
20 pts. - 10_1.py executes without error
60 pts. - Program meets requiments

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.
"""

'''HELPER METHODS - DO NOT EDIT '''
__guests = 'guests'
def check_book(gb):
    """make sure book is valid"""
    valid = gb is not None and __guests in gb
    if not valid:
        print('invalid guestbook format')
    return valid

def add_guest(guestbook, name):
    """add new guest"""
    if check_book(guestbook):
        new_obj = { "id" : len(guestbook[__guests]), "name":name }
        guestbook[__guests].insert(0, new_obj)
        print("new entry added\n")

def read_book(guestbook):
    """display entries"""
    if check_book(guestbook):
        all_guests = ['- {0}. {1}'.format(
            guest['id'], guest['name']) \
            for guest in guestbook[__guests]]
        print('\nRECENT GUESTS\n' + '\n'.join(all_guests) + '\n')
'''END'''

#=======================================================================
# ASSIGNMENT INSTRUCTIONS
#-----------------------------------------------------------------------
# JavaScript Object Notation (JSON) is a data format that can be used
# to exchange data between applications written in many languages, 
# including python. It is very helpful when storing complex objects,
# because by using JSON, we can save and restore the object state very
# easily between executions. In today's lab we will practice using JSON
# by writing a simple guestbook application. Your initial data file
# is provided to you and it is called `guestbook.json`.
# 
# STEPS
#
# 1. import json module. You will need it whenever you work with  
#    JSON formatted data.
#
# 2. Open `guestbook.json` for reading. Read its entire contents into
#    an object called `guestbook`. You will need to use json.loads() 
#    method to correctly parse the data. 
#-----------------------------------------------------------------------
import json

filename ="guestbook.json"
with open(filename) as guestbook:
	username = json.load(guestbook)
	
	
	





#-----------------------------------------------------------------------
# 3. Write a while loop that remains active until user decides to quit.
#    Prompt the user with 3 choices:
#    - sign guestbook
#    - read guestbook
#    - quit
#
# 4. If user wants to sign, prompt them for a name. Then call method 
#
#    add_guest(guestbook, name)
#
#    where name is the response you got from the user and guestbook
#    is a reference to the JSON object from step 2. This method is
#    already provided to you. After performing these steps, display
#    the 3 choices to user again.
#
# 5. If user chooses to read the guestbook, call method 
#
#    read_book(guestbook)
#
#    where guestbook is a reference to the JSON object from step 2.
#    This method is already provided to you. After performing these 
#    steps, display the 3 choices to user again.
#
# 6. If user wants to quit, break the while loop. 
#-----------------------------------------------------------------------

while True:
	user_response = input("Input one of the following: \n[1]Sign Guestbook \n[2]Read Guestbook \n[3]Quit")
	if user_response == str(1):
		name = input("What is your name")
		add_guest(username, name)
		
	elif user_response == str(2):
		read_book(username)
		
	else:
		break






#-----------------------------------------------------------------------
# 7. After the while loop, write the guestbook object to 
#    `guestbook.json` file, so data is not lost. You will need to use
#    json.dumps() method to correctly save the data.
#    After this step the program may terminate.
#
# 8. Run your program a couple of times and make sure your JSON
#    data reads and writes are working correctly and no data gets
#    lost between executions.
#-----------------------------------------------------------------------

with open (filename, 'w') as guestbook:
	json.dump(username, guestbook)



#=======================================================================
# That's it for today!
# End of Lab Exercise 10.1
#=======================================================================
